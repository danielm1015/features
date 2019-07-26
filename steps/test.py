from behave import *
import requests
from connectapi import ConnectAPI


@given('the Continuous Automated Build System exists')
def step_impl(context):
    print("This is the context string: "+ context.text)
   
    data = ConnectAPI(context.text)
    print(" Setting variable data with request connection: ", data)
    print(" Calling Getter to : ", data.connectAPI)
    

@when('I query the Ansible API for the CABS Operating System')
def step_impl(context):
    pass
    
@then('the API returns RHEL7')
def step_impl(context):
    pass

