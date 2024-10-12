import requests
import json
import sys

class ZOSMFManager:
    baseapiurl = "/ibmmq/rest/v1/messaging"
    
    def __init__(self, ep, cert_file_path, key_file_path):
        self.endpoint = ep
        self.cert = (cert_file_path, key_file_path) 

    def listfilesrequest(self, path):
        # operation = POST or DELETE
        resourceurl = self.endpoint + "/restfiles/fs?path=" + path 
        request_headers = {
            'Content-Type' : 'application/json;charset=utf-8' ,
            'X-CSRF-ZOSMF-HEADER' : 'somevalue',
            }
        data = {}
        response = requests.get(resourceurl, data=data, cert=self.cert, verify=False, headers=request_headers)
        return response


print('---------')

#cert_file_path = "/u/greefdn/pythonprograms/dwc-client-ssl-xat.crt"   
#key_file_path = "/u/greefdn/pythonprograms/dwc-client-ssl-xat.privkey"

cert_file_path = sys.argv[1]
key_file_path = sys.argv[2]

m1 = ZOSMFManager("https://zoswfx1-xat.zos.rabobank.nl:443/zosmf","", cert_file_path, key_file_path)

#https://zoswfx1-xat.zos.rabobank.nl:443/zosmf/restfiles/fs?path=/u/greefdn

response = m1.apigetrequest("/u/greefdn")

print(">>>", response.status_code, response.json)

print(response.headers) 

print(response)
msgid = response.headers['ibm-mq-md-messageId']
print(response.headers['ibm-mq-md-messageId'])

response = m1.apideleterequest("Q2X1","MQ00.TEST.MQWEB_NIEK.LQ", msgid) 
print(">>>", response.status_code, response.json)



print('---------')
