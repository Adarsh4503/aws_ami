""" PRE_REQUISITES
create a config.py file with 5 variables
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
    """

import os
import sys
import boto3
import config
import time

os.system('clear')

def inter(list1, list2):
    """
    function to find intersection between 2 lists
    returns - a list with intersecting values
    """
    return list(set(list1) & set(list2))

session = boto3.Session(
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key
    )

ec2 = session.resource('ec2')
ec2_client=session.client('ec2')
s3 = session.resource('s3',region_name=config.region)
s3_client=session.client('s3')


location = {'LocationConstraint': config.region}

try:
    bucket_check=s3.Bucket(config.bucket) in s3.buckets.all()
    if bucket_check==False:
        s3.create_bucket(Bucket=config.bucket,CreateBucketConfiguration=location)
        print(f"Bucket {config.bucket} created")
    time.sleep(1)
    try:
        s3_client.put_bucket_acl(
        Bucket=config.bucket,
        GrantFullControl=f'id="{config.grantee_id}"'
        )
    except Exception as error:
        print(error)
        time.sleep(1)
    
except Exception as error:
    print(error)
    sys.exit()

instance_id={}
instance_names={}
i=1

for instance in ec2.instances.all():
    for tag in instance.tags:
        instance_names[i]=tag['Value']

    instance_id[i]=instance.id
    i+=1

os.system('clear')
print("######INSTANCE NAMES#####")
for name in instance_names:
    print(f"{name}.{instance_names[name]}")

print("Enter the numbers corresponding to the instances of which you want AMI made ( Leave a space between each entry):")
inp = list(map(int, input().split()))

ami_instances=inter(instance_names.keys(),inp)

for inst in ami_instances:
    response=ec2_client.create_instance_export_task(
    Description='ami-image',
    ExportToS3Task={
        'DiskImageFormat': config.image_format,
        'S3Bucket': config.bucket,
        'S3Prefix': f'ami-{instance_names[inst]}--'
    },
    InstanceId=instance_id[inst],
    TargetEnvironment='vmware')
    
count=len(ami_instances)
status=0.1
while status<1:
    if (i-1)!=0:
        objs = s3_client.list_objects_v2(Bucket=config.bucket)
        fileCount = objs['KeyCount']-1
        status=fileCount/count
        print(f"Completion Percentage:{status*100}")
        time.sleep(10)
    else:
        objs = s3_client.list_objects_v2(Bucket=config.bucket)
        status = objs['KeyCount']-1
        print(f"Completion Percentage:{status*100}")
        time.sleep(10)

print("Completed")
