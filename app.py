#!/usr/bin/env python3
from aws_cdk import (
    App,
)

# wrapper stack to test our contruct during implementation
from stacks.ecr_stack import WrapperEcrStack

# stack that uses the final pip module, only comment out, once module is build and installed at least locally
from usage.ecr_stack import ClientEcrStack


app = App()

repos = ["repo1", "repo2"]
stage_account = "123456789012"
stack = WrapperEcrStack(app, "MyECRStack", stage_account, repos)

## once you have build and import the pip module you can comment out this code, which shows the usage of the pip module
# client_stack = ClientEcrStack(app, "MyClientECRStack", stage_account, repos)

app.synth()
