class ConnectAPI:
    
    @property
    def api_connect(self):
        print("In api_connect(self)")
        return self._response

    @api_connect.setter
    def api_connect(self, context):
        print("In api_connect(self, context)")
