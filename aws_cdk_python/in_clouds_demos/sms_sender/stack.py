from aws_cdk import (core, aws_lambda, aws_sns, aws_iam)


class SmsSenderStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        sender_lambda = aws_lambda.Function(
            self,
            "sms_sender_lambda", 
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler="sms_sender.handler",
            code=aws_lambda.Code.asset('in_clouds_demos/sms_sender/lambda'))

        sender_lambda.role.add_to_policy(aws_iam.PolicyStatement(actions=['sns:Publish'], resources=["*"]))
        