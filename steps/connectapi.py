from behave import *
import requests
import json

class ConnectAPI:
    
    def __init__(self, url):
        self.url = url
    
    def connectAPI(self):
        print("Setting Value")

        API_USER = ""
        API_PASSWD = ""

        user_pass = (API_USER, API_PASSWD)
        response = requests.get(self.url, auth=user_pass, verify=False)
        
        return json.loads(response.text)
