import sys
import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'
    
def lambda_handler(event, context):
  cwlogs = boto3.client('logs', region)
  response = cwlogs.list_tags_log_group(logGroupName='test1')
  print response
