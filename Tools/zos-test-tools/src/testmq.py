import requests
import json
import sys

class MQWebManager:
    baseapiurl = "/ibmmq/rest/v1/messaging"
    
    def __init__(self, ep, ak, cert_file_path, key_file_path):
        self.endpoint = ep
        self.apikey = ak
        self.cert = (cert_file_path, key_file_path) 

    def apideleterequest(self, qmgr, queue, msgid):
        # operation = POST or DELETE
        resourceurl = self.endpoint + "/ibmmq/rest/v1/messaging/qmgr/" + qmgr + "/queue/" + queue + "/message"
        request_headers = {
            'messageId': "'" + msgid + "'",
            'Content-Type' : 'text/plain;charset=utf-8' ,
            'ibm-mq-rest-csrf-token' : 'somevalue',
            'correlationId' : ''
            }
        data = {}
        response = requests.delete(resourceurl, data=data, cert=self.cert, verify=False, headers=request_headers)
        return response

    def apipostrequest(self, qmgr, queue):
        # operation = POST or DELETE
        resourceurl = self.endpoint + "/ibmmq/rest/v1/messaging/qmgr/" + qmgr + "/queue/" + queue + "/message"
        request_headers = {
            'Content-Type' : 'text/plain;charset=utf-8' ,
            'ibm-mq-rest-csrf-token' : 'somevalue'
            }
        data = 'hello from apipostrequest'
        print('resource url: ', resourceurl)
        response = requests.post(resourceurl, data=data, cert=self.cert, verify=False, headers=request_headers)
        return response



print('---------')

#cert_file_path = "/.../ssl.crt"   
#key_file_path = "/.../ssl.privkey"

cert_file_path = sys.argv[1]
key_file_path = sys.argv[2]

m1 = MQWebManager("https://your.mqweb-url:21541","", cert_file_path, key_file_path)


response = m1.apipostrequest("QMG1","QUEU.TEST.MQWEB_Q") 
print(">>>", response.status_code, response.json)

print(response.headers) 

print(response)
msgid = response.headers['ibm-mq-md-messageId']
print(response.headers['ibm-mq-md-messageId'])

response = m1.apideleterequest("QMG1","QUEU.TEST.MQWEB_Q", msgid) 
print(">>>", response.status_code, response.json)



print('---------')
