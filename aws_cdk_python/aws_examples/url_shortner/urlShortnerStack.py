from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as _apigw
)

class UrlShortnerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

    