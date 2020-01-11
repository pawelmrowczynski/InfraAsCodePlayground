import json
import boto3
import logging
import hashlib
import os

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)

def handler(event, context):
    LOG.info('Event payload: %s', json.dumps(event))

    query_string_params = event["queryStringParameters"]

    phone_number = query_string_params["phone"]
    message = query_string_params["message"]
    sender_id = query_string_params["senderId"]

    if phone_number is not None and message is not None and sender_id is not None:
        LOG.info("Sending sms message to %s, with sender id = %s",
                 phone_number, sender_id)
        table_name = os.environ.get('TABLE_NAME')
        message_hash = hashlib.md5(message.encode('utf-8')).hexdigest()
        sns = boto3.client('sns')
        sns.publish(PhoneNumber=f"+{phone_number}", Message=message, MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': sender_id
            }})
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)
        table.put_item(Item={
            'phoneNumber': phone_number,
            'messageHash': message_hash,
            'message': message,
            'senderId': sender_id
        })

    return {
        'statusCode': 200,
        'body': json.dumps(f'Message with id {message_hash} sent')
    }
