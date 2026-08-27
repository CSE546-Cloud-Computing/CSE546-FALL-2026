# Autograder for Project-0

Make sure that you use the provided autograder and follow the instructions below to test your project submission. Failure to do so may cause you to lose all the project points and there will be absolutely no second chance.

- Download the zip file you submitted from Canvas. 
- Download the autograder from GitHub: `https://github.com/CSE546-Cloud-Computing/CSE546-FALL-2026.git`
  - In order to clone the GitHub repository follow the below steps:
  - `git clone https://github.com/CSE546-Cloud-Computing/CSE546-FALL-2026.git` 
  - `cd CSE546-FALL-2026/`
  - `git checkout project-0`
- Create a directory `submissions` in the CSE546-FALL-2026 directory and move your zip file to the submissions directory.

## Prepare to run the autograder
- Install Python: `sudo apt install python3`
- Populate the `class_roster.csv`
  - If you are a student; replace the given template only with your details.
  - If you are a grader; use the class roster for the entire class

## Run the autograder
- Run the autograder: `python3 autograder.py`
- The autograder will look for submissions for each entry present in the class_roster.csv
- For each submission the autograder will
  - Validate if the zip file adheres to the submission guidelines as mentioned in the project document.
    - If Yes; proceed to next step
    - If No; allocate 0 grade points and proceed to the next submission
  - The autograder extracts the credentials.txt from the submission and parses the entries.
  - Use the Grader IAM credentials to test the project as per the grading rubrics and allocate grade points.
  - The autograder will dump stdout and stderr in a log file named autograder.log
      
## Sample Output

  ```
  +++++++++++++++++++++++++++++++ CSE546 Autograder  +++++++++++++++++++++++++++++++
  - 1) The script will first look up for the zip file following the naming conventions as per project document
  - 2) The script will then do a sanity check on the zip file to make sure all the expected files are present
  - 3) Extract the credentials from the credentials.txt
  - 4) Execute the test cases as per the Grading Rubrics
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  ++++++++++++++++++++++++++++ Autograder Configurations ++++++++++++++++++++++++++++
  Project Path: /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0
  Grade Project: Project-0
  Class Roster: class_roster.csv
  Zip folder path: /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/submissions
  Test zip contents script: /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/test_zip_contents.sh
  Grading script: /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/grade_project0.py
  Autograder Results: Project-0-grades.csv
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  ++++++++++++++++++ Grading for Doe John ASUID: 1225754101 +++++++++++++++++++++
  Executing /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/test_zip_contents.sh on /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/submissions/Project0-1225754101.zip
  /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/test_zip_contents.sh output:
  [log]: Look for credentials directory (credentials)
  [log]: - directory /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/unzip_1768930111/credentials found
  [log]: Look for credentials.txt
  [log]: - file /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/unzip_1768930111/credentials/credentials.txt found
  [test_zip_contents]: Passed

  Unzip submission and check folders/files: PASS
  Extracted /home/local/ASUAD/kjha9/git/git-CSE546/Autograder-Fall-2026/Project-0/submissions/Project0-1225754101.zip to extracted
  Following files were found in the zip: ['extracted/credentials/credentials.txt']
  This is the submission file path: extracted/credentials
  Found credentials.txt  at extracted/credentials
  File: extracted/credentials/credentials.txt has values ('XXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
  -------------- CSE546 Cloud Computing Grading Console -----------
  IAM ACESS KEY ID: XXXXXXXXXXXXXXXXXXXX 
  IAM SECRET ACCESS KEY: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
  -----------------------------------------------------------------
  [IAM-log] Following policies are attached with IAM user:cse546-AutoGrader: ['AWSGreengrassReadOnlyAccess', 'AWSIoTFullAccess', 'AmazonEC2ReadOnlyAccess', 'IAMReadOnlyAccess', 'AmazonS3ReadOnlyAccess', 'AmazonSQSReadOnlyAccess', 'AWSLambda_ReadOnlyAccess']
  [Cloudwatch-log] Alarm:Billing-alarm-5$ with ARN:arn:aws:cloudwatch:us-east-1:906986098922:alarm:Billing-alarm-5$ found in state:OK. It is configued with statistic:Maximum, threshold:5.0 and Comparison Operator:GreaterThanOrEqualToThreshold
  [Cloudwatch-log] Billing alarm:arn:aws:cloudwatch:us-east-1:906986098922:alarm:Billing-alarm-5$ is not triggered.
  [Cloudwatch-log] CAUTION !! You do not have a Cloudwatch alarm set. Kindly refer to the Project-0 document and learn how to set a billing alarm
  -----------------------------------------------------------------
  ----- Executing Test-Case:1 -----
  [EC2-log] AmazonEC2ReadOnlyAccess policy attached with grading IAM
  [EC2-log] Trying to create a EC2 instance
  [EC2-log] EC2 instance creation failed with UnauthorizedOperation error. This is as expected. Points:[33.33/33.33]
  ----- Executing Test-Case:2 -----
  [S3-log] AmazonS3ReadOnlyAccess policy attached with grading IAM
  [S3-log] Trying to create a S3 bucket
  [S3-log] Bucket creation failed with Access Denied error. This is expected. Points:[33.33/33.33]
  ----- Executing Test-Case:3 -----
  [SQS-log] AmazonSQSReadOnlyAccess policy attached with grading IAM
  [SQS-log] Trying to create a SQS queue
  [SQS-log] SQS creation failed with Access Denied error. This is expected. Points:[33.33/33.33]
  Total Grade Points: 100
  Removed extracted folder: extracted
  Execution Time for Doe John ASUID: 1225754101: 6.884997367858887 seconds
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  Grading complete for Project-0. Check the Project-0-grades.csv file
  ```
