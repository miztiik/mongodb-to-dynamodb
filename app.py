#!/usr/bin/env python3

from aws_cdk import core

from mongodb_to_dynamodb.mongodb_to_dynamodb_stack import MongodbToDynamodbStack


app = core.App()
MongodbToDynamodbStack(app, "mongodb-to-dynamodb")

app.synth()
