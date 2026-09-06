#!/usr/bin/env python3

from __future__ import annotations

__copyright__   = "Copyright 2026, VISA Lab"
__license__     = "MIT"

"""
File: sanity_checker.py
Author: Kritshekhar Jha
Description: CSE546 Project-1 Part-1 submission sanity checker.

Checks the ZIP layout without extracting it:
- the ZIP filename follows Project1-<ASUID>.zip, allowing the -1/-2 suffix
  Canvas appends on repeat submission attempts
- credentials/ and web-tier/ sit at the ZIP root, not inside a wrapper folder
- credentials/credentials.txt and web-tier/server.py are present, each directly
  inside its own directory rather than in a nested subdirectory
Usage:
    python3 sanity_checker.py Project1-1225754101.zip
"""

import argparse
import re
import zipfile
from pathlib import PurePosixPath

ZIP_NAME_RE    = re.compile(r"^Project1-(\d+)(?:-\d+)?\.zip$")
WRAPPER_DIR_RE = re.compile(r"^Project[-_ ]?1.*$", re.IGNORECASE)

EXPECTED_FILES = {
    "credentials/credentials.txt",
    "web-tier/server.py",
}
EXPECTED_DIRS = {
    "credentials",
    "web-tier",
}

ZIP_COMMAND = "zip -r Project1-<ASUID>.zip credentials/ web-tier/"


def normalize_name(name: str) -> str:
    """Normalize ZIP entry names for comparison without extracting them.

    Only a leading './' is stripped. Leading '/' and '..' are deliberately left
    in place so that check_submission() can still flag them as suspicious.
    """
    name = name.replace("\\", "/")
    while name.startswith("./"):
        name = name[2:]
    return name


def is_file_entry(info: zipfile.ZipInfo) -> bool:
    """Return True for file entries, excluding directory entries."""
    return not info.is_dir() and not info.filename.endswith("/")


def is_archive_metadata(entry: str) -> bool:
    """Junk the macOS Archive Utility and Finder add to a ZIP."""
    basename = entry.rsplit("/", 1)[-1]
    return (
        entry.startswith("__MACOSX/")
        or basename == ".DS_Store"
        or basename.startswith("._")
    )


def check_submission(zip_path: str) -> tuple[bool, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    filename = PurePosixPath(zip_path).name
    if not ZIP_NAME_RE.fullmatch(filename):
        errors.append(
            f"Invalid ZIP filename: {filename}. Expected Project1-<ASUID>.zip "
            "(for example Project1-1225754101.zip)."
        )

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            if zf.testzip() is not None:
                errors.append("ZIP contains a file with a CRC error.")

            entries      = [normalize_name(info.filename) for info in zf.infolist()]
            file_entries = {
                normalize_name(info.filename)
                for info in zf.infolist()
                if is_file_entry(info)
            }
            directory_entries = {e.rstrip("/") for e in entries if e.endswith("/")}
            top_levels        = sorted({e.split("/", 1)[0] for e in entries if e})

            for item in top_levels:
                if WRAPPER_DIR_RE.fullmatch(item):
                    errors.append(
                        f"Unexpected wrapper directory: {item}/. "
                        "Put credentials/ and web-tier/ directly at the ZIP root."
                    )

            # A directory counts as present if it has an explicit entry or any file under it,
            # since `zip` does not always emit standalone directory entries.
            for item in sorted(EXPECTED_DIRS):
                if item not in directory_entries and not any(
                    entry.startswith(f"{item}/") for entry in file_entries
                ):
                    errors.append(f"Missing required directory: {item}/")

            for item in sorted(EXPECTED_FILES - file_entries):
                errors.append(f"Missing required file: {item}")

            # The project document is explicit that extra files cost points, so
            # anything outside the expected set fails rather than warns.
            found_metadata = False
            for item in sorted(file_entries - EXPECTED_FILES):
                if is_archive_metadata(item):
                    found_metadata = True
                    errors.append(f"Archive metadata file found: {item}")
                elif len(item.split("/")) > 2:
                    errors.append(
                        f"File in a nested subdirectory: {item}. credentials.txt must sit "
                        "directly in credentials/ and server.py directly in web-tier/."
                    )
                else:
                    errors.append(
                        f"Unwanted file found: {item}. "
                        "The project document says not to submit any other files."
                    )

            if found_metadata:
                warnings.append(
                    "Rebuild without the macOS metadata: "
                    f"{ZIP_COMMAND} -x '__MACOSX/*' '*.DS_Store'"
                )

            # Basic protection against suspicious ZIP paths. These should not be present
            # in a valid submission, even though this checker never extracts the archive.
            for item in sorted(
                e for e in file_entries if e.startswith("/") or ".." in e.split("/")
            ):
                errors.append(f"Suspicious ZIP path: {item}")

    except FileNotFoundError:
        errors.append(f"File not found: {zip_path}")
    except zipfile.BadZipFile:
        errors.append("The selected file is not a valid ZIP archive.")
    except PermissionError:
        errors.append(f"Permission denied: {zip_path}")
    except OSError as exc:
        errors.append(f"Could not read ZIP: {exc}")

    return not errors, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="CSE546 Project-1 Part-1 ZIP sanity checker")
    parser.add_argument("zip_file", help="Path to the Project-1 Part-1 submission ZIP")
    args = parser.parse_args()

    passed, errors, warnings = check_submission(args.zip_file)

    print("=" * 72)
    print("CSE546 Project-1 Part-1 - Submission Sanity Check")
    print("=" * 72)
    print(f"ZIP: {args.zip_file}")

    if passed:
        print("\nPASS")
        print("The ZIP structure matches the Project-1 Part-1 requirements.")
        print("\nExpected files:")
        for item in sorted(EXPECTED_FILES):
            print(f"  [ok] {item}")
    else:
        print("\nFAIL")
        for message in errors:
            print(f"  [!!] {message}")

    if warnings:
        print("\nNotes:")
        for message in warnings:
            print(f"  [--] {message}")

    if not passed:
        print("\nExpected structure:")
        print("  Project1-<ASUID>.zip")
        print("  |-- credentials/")
        print("  |   `-- credentials.txt")
        print("  `-- web-tier/")
        print("      `-- server.py")
        print("\nBuild the ZIP from the directory holding credentials/ and web-tier/:")
        print(f"  {ZIP_COMMAND}")

    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
