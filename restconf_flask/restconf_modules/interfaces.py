import requests
import json

requests.packages.urllib3.disable_warnings()

class InterfaceInfo(object):
    headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json", 
      }

    module="ietf-interfaces:interfaces"


    def __init__(self,Host,Port,Username,Password):
        
        self.device={
            'host':Host,
            'username': Username,
            'password': Password,
            'port':Port
            }
        self.response = self.make_request()
        self.get_interfaces()
        
    def make_request(self):
        url=f"https://{self.device['host']}:{self.device['port']}/restconf/data/{self.module}"
        request = requests.get(url,auth=(self.device['username'],self.device['password']),headers=self.headers,verify=False)
        return request.json()
    
    def get_interfaces(self):
        interfaces={}
        for interface in self.response['ietf-interfaces:interfaces']['interface']:
            try:
                interface_name=interface['name']
                interface_description= interface['description']
                interface_enabled=interface['enabled']
                interface_address= interface['ietf-ip:ipv4']['address'][0]['ip']
            except KeyError as error:
                interface_description= 'No Description Configured'
                interface_address= 'No Address configured '
            interfaces[interface_name]={
                                        'description':interface_description,
                                        'address':interface_address,
                                        'enabled':interface_enabled}
        return interfaces
        
