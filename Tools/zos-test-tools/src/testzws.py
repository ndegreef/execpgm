import requests

print("tested")


print("hello") 

host = "https://xiws.zos.yourco.nl:1603"
baseapiurl = "/twsz" 
getrequest = "/v1/SJXT/engine/info"
api_url = host + baseapiurl + getrequest
print(api_url)

request_headers = {
    'Content-Type': 'application/json'
}

cert_file_path = "/u/greefn/pythonprograms/dwc-client-ssl-xat.crt"
key_file_path = "/u/greefn/pythonprograms/dwc-client-ssl-xat.privkey"
cert = (cert_file_path, key_file_path)
# data = {'api_dev_key':API_KEY,
#        'api_option':'paste',
#        'api_paste_code':source_code,
#        'api_paste_format':'python'}

data = """{
  "hasDatabasePlan": true,
  "locale": "string",
  "timezone": "string",
  "timezoneEnable": true,
  "roleBasedSecurityEnabled": true,
  "type": "string",
  "version": "string",
  "apiLevel": 0,
  "featureLevel": 0,
  "hasModel": true,
  "hasPlan": true,
  "enableRerunOpt": true,
  "engineType": "string",
  "ltpStartDate": "2022-02-16T13:48:01.978Z",
  "ltpEndDate": "2022-02-16T13:48:01.978Z",
  "dbTimezone": "string",
  "planTimezone": "string",
  "workstationName": "string",
  "domainName": "string",
  "synphonyRunNumber": 0,
  "synphonyScheduledDate": "2022-02-16T13:48:01.978Z",
  "synphonyBatchManStatus": "string",
  "synphonyStartOfDay": 0,
  "masterDomain": "string",
  "masterWorkstation": "string",
  "synphonyFileName": "string",
  "synphonyPlanStart": "2022-02-16T13:48:01.978Z",
  "synphonyPlanEnd": "2022-02-16T13:48:01.978Z",
  "synphonySize": 0,
  "synphonyStartTime": "2022-02-16T13:48:01.978Z",
  "synphonyFound": true,
  "enableLegacyStartOdDayEvaluation": true,
  "dbStartOfDay": "string",
  "rdbmsSchema": "string",
  "rdbmsUser": "string",
  "rdbmsType": "string",
  "rdbmsUrl": "string",
  "fipsEnabled": true,
  "regardlessOfStatusFilterEnabled": true,
  "executorList": [
    {
      "application": "string",
      "namespace": "string",
      "version": "string",
      "factory": "string",
      "supportedOS": "string",
      "stoppable": true,
      "restartable": true,
      "labels": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "id": "string",
      "xsdResourceName": "string",
      "cancelSupported": true,
      "supportedWorkstation": "string"
    }
  ],
  "auditStore": "string",
  "auditModel": "string",
  "auditPlan": "string",
  "licenseType": "string",
  "licenseJobNumber": 0,
  "licenseSendDate": 0,
  "wasFirstStartDate": 0,
  "licenseError": "string"
}"""


#response = requests.post(api_url, data = data, auth=('GREEFN', 'password'), verify=False) cert=cert



try:
    #response = requests.get(api_url, auth=('GREEFN', 'password'), verify=False, headers=request_headers)
    response = requests.get(api_url, cert=cert, verify=False, headers=request_headers)

except requests.exceptions.RequestException as e:
    print(e)

#response.json()
print('---------')

print(response)
print('---------')
print(response.json())
print('---------')