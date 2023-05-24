#PRE_REQUISITES
-Install boto3
.
##create a config.py file with 5 variables
1.aws_access_key_id        - from aws console
2.aws_secret_access_key    - from aws console
3.region                   - region in which the ec2 is present
4.bucket                   - name of the bucket in which you want the images
5.image_format             - VMDK |VHD | RAW
6.grantee_id               - c4d8eabf8db69dbe46bfe0e517100c554f01200b104d59cd408e777ba442a322
                             unless you're targeting an S3 bucket in Bahrain, Hong Kong, Beijing,
                             or GovCloud (US-West), which have different grantees.
                             See the docs
                             https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html
                             
enter the values in the file and save it where you run this script
    
