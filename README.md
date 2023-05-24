# GENERAL
This function helps to export ec2 instances into vmdk vhk or raw format into an S3 bucket which is created via this script itself.

## PRE_REQUISITES
- Install boto3

- Attach the following policy to your amazon account ( enter your bucket name at mys3bucket }
    ```
    {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": ["arn:aws:s3:::mys3bucket","arn:aws:s3:::mys3bucket/*"]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CancelConversionTask",
        "ec2:CancelExportTask",
        "ec2:CreateImage",
        "ec2:CreateInstanceExportTask",
        "ec2:CreateTags",
        "ec2:DescribeConversionTasks",
        "ec2:DescribeExportTasks",
        "ec2:DescribeExportImageTasks",
        "ec2:DescribeImages",
        "ec2:DescribeInstanceStatus",
        "ec2:DescribeInstances",
        "ec2:DescribeSnapshots",
        "ec2:DescribeTags",
        "ec2:ExportImage",
        "ec2:ImportInstance",
        "ec2:ImportVolume",
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:TerminateInstances",
        "ec2:ImportImage",
        "ec2:ImportSnapshot",
        "ec2:DescribeImportImageTasks",
        "ec2:DescribeImportSnapshotTasks",
        "ec2:CancelImportTask"
      ],
      "Resource": "*"
    }
  ]
}

### Create a config.py file with 5 variables
1. aws_access_key_id        - from aws console
2. aws_secret_access_key    - from aws console
3. region                   - region in which the ec2 is present
4. bucket                   - name of the bucket in which you want the images
5. image_format             - VMDK |VHD | RAW
6. grantee_id               - **c4d8eabf8db69dbe46bfe0e517100c554f01200b104d59cd408e777ba442a322**
    
    unless you're targeting an S3 bucket in Bahrain, Hong Kong, Beijing,
    or GovCloud (US-West), which have different grantees.
    
    See the docs:
    https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html
                             
**enter the values in the file and save it where you run this script**
    
PS Currently, the script has a slight error and after running the script once please go to the bucket created and enable ACL
and run the script again. Will try to fix this when i get time.
