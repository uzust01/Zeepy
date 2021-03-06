'''
Copyright 2020 Guilherme Cartier de Palma

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 
'''

from ..utilities import ZosmfApi
import requests

class Zosmf(ZosmfApi):

    def __init__(self, connection):
        super().__init__(connection, '/zosmf/info')

    def get_info(self):
        response = requests.get(self.request_endpoint, 
                                verify=self.connection.ssl_verification,
                                timeout=30)
        return self.response_handler.validate_response(response, 200)

        
