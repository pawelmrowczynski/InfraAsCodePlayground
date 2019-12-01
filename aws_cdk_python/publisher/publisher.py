import json
import random
import os
import boto3

def handler(event, context):
    random_number = str(random.randint(1, 1000))
    queue_url = os.environ['QUEUE_URL']
    sqs = boto3.client('sqs')
    print(f"Randomly generated {random_number}, publishing to {queue_url}")
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=(
            random_number
        )
    )

    print(f"Succesfully wrote message to sqs. MessageId: {response['MessageId']}")