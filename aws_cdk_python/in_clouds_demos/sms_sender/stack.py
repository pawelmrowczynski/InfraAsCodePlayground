from aws_cdk import (core, aws_lambda, aws_sns, aws_iam, aws_dynamodb, aws_apigateway)
from cdk_watchful import Watchful

class SmsSenderStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        sender_lambda = aws_lambda.Function(
            self,
            "sms_sender_lambda",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler="sms_sender.handler",
            code=aws_lambda.Code.asset('in_clouds_demos/sms_sender/lambda'))

        # Api Gateway
        api = aws_apigateway.LambdaRestApi(self, "SmsSenderApi",
                                           handler=sender_lambda)
        # DynamoDb Table
        # indeks = phone number, secondary index md5 z contentu?
        table = aws_dynamodb.Table(
            self,
            "message_log",
            partition_key=aws_dynamodb.Attribute(name="phoneNumber", type=aws_dynamodb.AttributeType.NUMBER),
            sort_key=aws_dynamodb.Attribute(name="messageHash", type=aws_dynamodb.AttributeType.STRING),
            removal_policy=core.RemovalPolicy.DESTROY)

        sender_lambda.add_environment('TABLE_NAME', table.table_name)
        table.grant_read_write_data(sender_lambda)


        sender_lambda.role.add_to_policy(aws_iam.PolicyStatement(
            actions=['sns:Publish'], resources=["*"]))
        
        wf = Watchful(self, "monitoring", alarm_email="pmrowka3@gmail.com")
        wf.watch_scope(self)
