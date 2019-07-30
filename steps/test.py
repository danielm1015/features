from behave import given, when, then, step
import requests
from connectapi import ConnectAPI


@given('the Continuous Automated Build System exists')
def step_impl(context):
    #print("This is the context string: "+ context.text)
    
    request = ConnectAPI(context.text)
   
    # print(" Setiting variable data with request connection: ", request)
    # print("Printing: json(): ", request.connectAPI())
    
    res = request.connectAPI()
    print("This is the sorted JSON file:\n")
    for i in sorted(res):
        print((i, res[i]), end= " ")


@when('I query the Ansible API for the CABS Operating System')
def step_impl(context):
    pass
    
@then('the API returns RHEL7')
def step_impl(context):
    pass

