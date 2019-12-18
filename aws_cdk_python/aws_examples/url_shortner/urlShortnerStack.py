from aws_cdk import core, aws_dynamodb, aws_lambda, aws_apigateway
from .myCoreStack import MyCoreStack

class UrlShortnerStack(MyCoreStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = aws_dynamodb.Table(
            self, 
            "mapping-table",
            partition_key = aws_dynamodb.Attribute(name="id", type = aws_dynamodb.AttributeType.STRING))
        
        function = aws_lambda.Function(
            self, "backend",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            handler = "handler.main",
            code = aws_lambda.Code.asset("aws_examples/url_shortner/lambda"))
        table.grant_read_write_data(function)

        function.add_environment("TABLE_NAME", table.table_name) ## late binding at provisioning time

        api = aws_apigateway.LambdaRestApi(self, "api", handler = function)

from .trafic_sim import TraficSim

class TrafficStack(MyCoreStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs) 