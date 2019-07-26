from behave import *
import requests

class ConnectAPI():
    
    def __init__(self, response):
        self._data = data

    @property
    def connectAPI(self):
        print("Getting Value")
        return self._data

    @connectAPI.setter
    def connectAPI(self, context):
        print("Setting Value")

        URL = context
        API_USER = "user"
        API_PASSWD = "password"

        user_pass = (API_USER, API_PASSWD)
        response = requests.get(URL, auth=user_pass, verify=False)
        
        self._data = response.json()
