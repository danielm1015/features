from behave import *
import requests
from connectapi import ConnectAPI

@given('the Continuous Automated Build System exists')
def step_impl(context):
    print("context string: "+ context.text)

@when('I query the Ansible API for the CABS Operating System')
def step_impl(context):
    pass
    
@then('the API returns RHEL7')
def step_impl(context):
    pass

