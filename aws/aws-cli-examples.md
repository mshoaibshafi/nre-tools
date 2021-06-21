# AWS CLI

## Instance Types 

Verify if "t3.micro" supported in all AZs in us-east-1

<code> aws ec2 describe-instance-type-offerings --location-type availability-zone  --filters Name=instance-type,Values=t3.micro --region us-east-1 --output table


<output>
-------------------------------------------------------
|            DescribeInstanceTypeOfferings            |
+-----------------------------------------------------+
||               InstanceTypeOfferings               ||
|+--------------+--------------+---------------------+|
|| InstanceType |  Location    |    LocationType     ||
|+--------------+--------------+---------------------+|
||  t3.micro    |  us-east-1f  |  availability-zone  ||
||  t3.micro    |  us-east-1c  |  availability-zone  ||
||  t3.micro    |  us-east-1d  |  availability-zone  ||
||  t3.micro    |  us-east-1b  |  availability-zone  ||
||  t3.micro    |  us-east-1a  |  availability-zone  ||
|+--------------+--------------+---------------------+|