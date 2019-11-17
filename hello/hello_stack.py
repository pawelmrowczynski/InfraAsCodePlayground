from aws_cdk import (
    aws_lambda as _lambda,
    core
)

from .hello_construct import HelloConstruct


class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        _lambda.
