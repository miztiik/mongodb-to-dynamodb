#!/usr/bin/env python3

from aws_cdk import core

from mongodb_to_dynamodb.stacks.back_end.vpc_stack import VpcStack
from mongodb_to_dynamodb.stacks.back_end.database_migration_prerequisite_stack import DatabaseMigrationPrerequisiteStack
from mongodb_to_dynamodb.stacks.back_end.mongodb_on_ec2_stack import MongodbOnEc2Stack


app = core.App()
# VPC Stack for hosting Secure API & Other resources
vpc_stack = VpcStack(
    app,
    "vpc-stack",
    description="Miztiik Automation: VPC to host resources for DB Migration"
)


# Build the pre-reqs for MongoDB on EC2
database_migration_stack = DatabaseMigrationPrerequisiteStack(
    app,
    "database-migration-prerequisite-stack",
    stack_log_level="INFO",
    vpc=vpc_stack.vpc,
    description="Miztiik Automation: DMS Best Practice Demonstration. This stack will create roles and security groups to assist in database migration"
)

# Deploy MongoDB on EC2
mongodb_on_ec2 = MongodbOnEc2Stack(
    app,
    "mongodb-on-ec2",
    vpc=vpc_stack.vpc,
    ec2_instance_type="t3.medium",
    stack_log_level="INFO",
    description="Miztiik Automation: Deploy MongoDB on EC2"
)
# Stack Level Tagging
core.Tag.add(app, key="Owner",
             value=app.node.try_get_context("owner"))
core.Tag.add(app, key="OwnerProfile",
             value=app.node.try_get_context("github_profile"))
core.Tag.add(app, key="Project",
             value=app.node.try_get_context("service_name"))
core.Tag.add(app, key="GithubRepo",
             value=app.node.try_get_context("github_repo_url"))
core.Tag.add(app, key="Udemy",
             value=app.node.try_get_context("udemy_profile"))
core.Tag.add(app, key="SkillShare",
             value=app.node.try_get_context("skill_profile"))
core.Tag.add(app, key="AboutMe",
             value=app.node.try_get_context("about_me"))
core.Tag.add(app, key="BuyMeACoffee",
             value=app.node.try_get_context("ko_fi"))
app.synth()
