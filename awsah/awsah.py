#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Gonzalo Alvarez

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from loguru import logger
import boto3
import json
import urllib
import requests
import time

def list_profiles():
    logger.warning("Listing profiles")
    for profile in boto3.session.Session().available_profiles:
        print(f"  {profile}")

def list_roles(profile):
    logger.info(f"Listing roles for profile [{profile}]")
    session = boto3.Session(profile_name=profile)
    iam = session.client('iam')
    roles = iam.list_roles()
    for role in roles['Roles']:
        print(f" Name: {role['RoleName']}  -- Arn: [{role['Arn']}]")

def show_account_info(profile):
    logger.info(f"Listing roles for profile [{profile}]")
    session = boto3.Session(profile_name=profile)
    sts = session.client('sts')
    caller_identity = sts.get_caller_identity()
    print(f"Account id: {caller_identity['Account']}")

def show_account_url(profile, role):
    logger.info(f"Accessing account URL for profile [{profile}]")
    session = boto3.Session(profile_name=profile)
    sts = session.client('sts')
    account_id = sts.get_caller_identity()['Account']
    assumed_role_object = sts.assume_role(
        RoleArn="arn:aws:iam::" + account_id + ":role/" + role,
        RoleSessionName= profile + "-" + role,
    )
    credentials = assumed_role_object.get('Credentials')
    session = json.dumps({'sessionId': credentials['AccessKeyId'],
                          'sessionKey': credentials['SecretAccessKey'],
                          'sessionToken': credentials['SessionToken']})

    r = requests.get("https://signin.aws.amazon.com/federation",
                     params={'Action': 'getSigninToken',
                             'SessionDuration': 43200,
                             'Session': session})
    signin_token = r.json()

    console = requests.Request('GET',
                              'https://signin.aws.amazon.com/federation',
                              params={'Action': 'login',
                                      'Issuer': 'AWS Access Helper',
                                      'Destination': 'https://console.aws.amazon.com/',
                                      'SigninToken': signin_token['SigninToken']})
    prepared_link = console.prepare()
    print(prepared_link.url)

def create_role(profile, role_name):
    logger.info(f"Creating a new role name {role_name}")
    session = boto3.Session(profile_name=profile)
    iam = session.client('iam')
    sts = session.client('sts')
    account_id = sts.get_caller_identity()['Account']
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {
                    "AWS": f"arn:aws:iam::{account_id}:root"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    tags = [
        {
            'Key': 'Environment',
            'Value': 'Production'
        }
    ]

    response = iam.create_role(
        Path="/",
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description="",
        MaxSessionDuration=3600,
        Tags=tags
    )
    print(response)
    time.sleep(5)
    logger.info("Attaching Policy")
    response = iam.attach_role_policy(
        RoleName=role_name, PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess")
    print(response)

