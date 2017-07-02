#!/usr/bin/env python
import json
import ssl
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def writethis(text,token_id,):
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	# API V2, send message to room:
	url = 'https://jira.rbc.ru/rest/api/2/issue/'
	headers = {
    "content-type": "application/json",
    "Authorization": "Basic bXNodXJzaGluOnBhcGtvc2RhbENDTkEy"}
	datastr = json.dumps({
    "fields": {
       "project":
       { 
          "key": "DEVOPSDUTY"
       },
       "summary": text,
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "name": "Bug"
       }
   }
})
	request = requests.post(url, headers=headers, data=datastr, verify=False)
	print request
