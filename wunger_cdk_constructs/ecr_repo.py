from constructs import Construct
import aws_cdk.aws_iam as iam
import aws_cdk as cdk
from aws_cdk import aws_ecr


class WUngerEcrConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        name: str,
        account: str,
        policy: iam.PolicyStatement,
        **kwargs,
    ):
        super().__init__(scope, id)

        self.repo = aws_ecr.Repository(self, f"{name}-{account}", repository_name=name)
        self.repo.add_to_resource_policy(policy)
