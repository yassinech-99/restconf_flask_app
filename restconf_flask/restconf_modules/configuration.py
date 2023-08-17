import requests
import json
import os


requests.packages.urllib3.disable_warnings()


class Configuration(object):

    headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json", 
      }
    module='Cisco-IOS-XE-native:native'


    def __init__(self,Host,Port,Username,Password):
        self.device={
            'host':Host,
            'username': Username,
            'password': Password,
            'port':Port
            }
        self.response= self.make_request()
        self.get_configuration()
        
    def make_request(self):
        url=f"https://{self.device['host']}:{self.device['port']}/restconf/data/{self.module}"
        request= requests.get(url,auth=(self.device['username'],self.device['password']),headers=self.headers,verify=False)
        return request.json()
    
    def get_configuration(self):
        
        output_folder= 'config-files'
        output_file=f"{self.device['host']}-config.json"
        os.makedirs(output_folder,exist_ok=True)
        output_path=os.path.join(output_folder,output_file)
        configuration_respone=self.response
        with open(output_path,"w") as config_file:
            config_file.write(json.dumps(configuration_respone,indent=4))

    def display_configuration(self):
        
        output_folder= 'config-files'
        output_file=f"{self.device['host']}-config.json"
        os.makedirs(output_folder,exist_ok=True)
        output_path=os.path.join(output_folder,output_file)
        configuration_respone=self.response
        with open(output_path,"r") as config_file:
            return config_file.read()

    
        
       
    
        
            
