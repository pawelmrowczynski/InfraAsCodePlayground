import os
from aws_cdk.core import Stack, Construct, Environment
from aws_cdk import aws_apigateway, aws_route53, aws_route53_targets, aws_certificatemanager, aws_ec2

# we need default values here since aws-cdk-examples build synthesizes the app
ACCOUNT=os.environ.get('CORE_ACCOUNT', '722785552123')
REGION=os.environ.get('CORE_REGION', 'eu-west-1')
VPC_ID = os.environ.get('CORE_VPC_ID', 'vpc-011c1dff6f9c0210f')

AWS_ENV = Environment(account=ACCOUNT, region=REGION)

class MyCoreStack(Stack):
    """
    A base CDK stack class for all stacks defined in our fun little company.
    """

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, env=AWS_ENV, **kwargs)

        # lookup our pre-created VPC by ID
        self._vpc = aws_ec2.Vpc.from_lookup(scope = self, id = "vpc", vpc_id=VPC_ID)

    @property
    def core_vpc(self) -> aws_ec2.IVpc:
        """
        :return: The my core vpc
        """
        return self._vpc


__all__ = ["coreStack"]