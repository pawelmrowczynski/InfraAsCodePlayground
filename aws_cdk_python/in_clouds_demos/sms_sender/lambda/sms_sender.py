import json
import boto3

def handler(event, context):
    sns = boto3.client('sns')
    number = '+48512261197'
    sns.publish(PhoneNumber=number, Message='Zordon Wzywa', MessageAttributes={
        'AWS.SNS.SMS.SenderID': {
            'DataType': 'String',
            'StringValue': 'Zordon'
        }})

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
