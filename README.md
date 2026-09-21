## Project 1 Part 2 Sanity Checker

Use `sanity_checker.py` to check the structure of your Project 1 Part 2 submission zip before submitting it.

Run the checker with:

```bash
python3 sanity_checker.py Project1-<ASUID>.zip
```

For example:

```bash
python3 sanity_checker.py Project1-1225754101.zip
```

## Expected Zip Name

Your zip file must be named:

```text
Project1-<ASUID>.zip
```

Replace `<ASUID>` with your ASU ID.

## Expected Zip Contents

The zip should contain the project folders directly at the root of the archive. Do not put everything inside an extra `Project1-<ASUID>/` folder, and do not nest the files in subfolders.

Expected structure:

```text
Project1-<ASUID>.zip
├── credentials/
│   └── credentials.txt
├── web-tier/
│   ├── server.py
│   └── controller.py
└── app-tier/
    └── backend.py
```

`credentials.txt` must hold the following values, separated by commas, in this order:

1. ACCESS KEY ID of the grading IAM user
2. SECRET ACCESS KEY of the grading IAM user
3. Elastic IPv4 address of the web tier

Do not submit any additional Python files.

## Creating The Zip

From the directory that contains `credentials/`, `web-tier/`, and `app-tier/`, run:

```bash
zip -r Project1-<ASUID>.zip credentials/ web-tier/ app-tier/
```

Then run the sanity checker:

```bash
python3 sanity_checker.py Project1-<ASUID>.zip
```

A `PASS` result means the zip structure matches the expected Project 1 Part 2 submission format. A `FAIL` result lists the missing, unwanted, or incorrectly placed files that need to be fixed.

## Workload Generator

`workload_generator.py` uploads images to a running web tier and reports how many requests completed, how many predictions matched the reference results, and the total test duration.

```bash
python3 workload_generator.py --num_request=100 --ip_addr=<web-tier-ip> \
    --image_folder=<path to the test images> --prediction_file=<path to the classification csv>
```

The web tier is expected to be listening on port 8000. Each run picks a different random subset of the images in `--image_folder`. Requires `requests` and `pandas`.
