from aws_cdk import (
    core
)

import aws_cdk.aws_ec2 as ec2

from .hello_construct import HelloConstruct

class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "CloudYourselfVpc", cidr= "10.0.0.0/16")
        
