from aws_cdk import (
    core
)

import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_lambda as _lambda

from .hello_construct import HelloConstruct

class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler',
        )
        
