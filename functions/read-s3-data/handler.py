import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def read_s3_data(event, context):
    try:
        # Log the received event
        logger.info(f"Received event: {json.dumps(event)}")

        # Extract bucket name and object key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        
        # Read the S3 object
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        data = response['Body'].read().decode('utf-8') # Adjust decoding as needed

        logger.info(f"Read data from {object_key}: {data}")
    except Exception as e:
        logger.error(f"Error processing S3 event: {e}")
        raise e
