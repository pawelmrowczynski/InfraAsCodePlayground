import json
import os
import boto3

def handler(event, context):
    for record in event['Records']:

        payload=record["body"]

        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

        table = dynamodb.Table(os.environ['TABLE_NAME'])

        response = table.put_item(
            Item={
                    "id": int(payload)
                }
        )

        print("PutItem succeeded:")
        print(json.dumps(response))