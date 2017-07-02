#!/usr/bin/env python
import json
import ssl
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def new(rname,rtopic,token_id):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    V2TOKEN = token_id
    url = 'https://hipchat.rbc.ru/v2/room'
    headers = {
    "content-type": "application/json",
    "authorization": "Bearer %s" % V2TOKEN}
    datastr = json.dumps({
    'name': rname.replace("!create", ""),
    'topic': rtopic})
    request = requests.post(url, headers=headers,  data=datastr, verify=False)
    msg=json.loads(request.content)
    try:
     return msg['id']
    except:
     return "Error %s" %msg
   