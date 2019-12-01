from aws_cdk import (
    core
)

import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_sqs as _sqs
import aws_cdk.aws_dynamodb as _dynamodb
import aws_cdk.aws_apigateway as _apigateway

class ProjectOneStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        queue = _sqs.Queue(self, "queue", queue_name="queue")
        table = _dynamodb.Table(self, "table", partition_key=_dynamodb.Attribute(name="id", type=_dynamodb.AttributeType.NUMBER))
        
        publisherFunction = _lambda.Function(
            self,
            'publisher',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('publisher'),
            handler='publisher.handler',
            environment={"QUEUE_URL":queue.queue_url}
        )

        apiGateway = _apigateway.RestApi(
            self,
            "api",
            deploy_options= _apigateway.StageOptions(stage_name="dev")
        )
        lambad_integration = _apigateway.LambdaIntegration(publisherFunction)

        apiGateway.root.add_method('GET', lambad_integration)

        subscriberFunction = _lambda.Function(
            self,
            'subscriber',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('subscriber'),
            handler='subscriber.handler',
            environment={
                "QUEUE_URL":queue.queue_url,
                "TABLE_NAME":table.table_name
                }
        )

        queue.grant_send_messages(publisherFunction)
        table.grant(subscriberFunction, "dynamodb:PutItem")
