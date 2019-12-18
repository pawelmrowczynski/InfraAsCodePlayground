#!/usr/bin/env python3

from aws_cdk import core

from hello.hello_stack import MyStack
from projectOne.main import ProjectOneStack
from aws_examples.api_cors_lambda.stack import ApiCorsLambdaStack
from aws_examples.url_shortner.urlShortnerStack import UrlShortnerStack
from aws_examples.url_shortner.urlShortnerStack import TrafficStack


app = core.App()
#base stack that you create in first tutorial
MyStack(app, "hello-cdk-1", env={'region': 'eu-west-1'})

# my first project, see readme.md for more details
ProjectOneStack(app, "project-one-stack", env={'region':'eu-west-1'})

# first example from aws-cdk-examples: https://github.com/aws-samples/aws-cdk-examples/tree/master/python/api-cors-lambda/
ApiCorsLambdaStack(app, "first-example-stack", env={'region':'eu-west-1'})

#url shortner stack
UrlShortnerStack(app, "url-shortner-stack")
TrafficStack(app, "test-trafick")

app.synth()
