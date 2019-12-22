from aws_cdk import (
    core,
    aws_apigateway as apigw
)

import aws_cdk.aws_lambda as _lambda

from hitcounter import HitCounter


class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('hello/lambda'),
            handler='hello.handler'
        )

        counter = HitCounter(self, "hello-hit-counter", my_lambda)

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=counter.handler,
        )
