from constructs import Construct
import aws_cdk.aws_iam as iam
import aws_cdk as cdk
from wunger_cdk.ecr_repo import WUngerEcrConstruct


class ClientEcrStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        stage_account: str,
        repos: list,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, description="WUnger ECR Stack", **kwargs)

        policy = iam.PolicyStatement(
            actions=[
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchDeleteImage",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:DescribeRepositories",
                "ecr:DescribeImages",
                "ecr:GetAuthorizationToken",
                "ecr:ListImages",
            ],
            effect=iam.Effect.ALLOW,
            principals=[iam.AccountPrincipal(stage_account)],
        )

        for repo in repos:
            ecr_repo = WUngerEcrConstruct(
                self,
                f"ecr-repo-{repo}",
                repo,
                stage_account,
                policy,
            )
