#!/usr/bin/env python
import json
import ssl
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def getlast(rid, token_id):
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	V2TOKEN = token_id
	#ROOMID = input('Enter room ID: ')
	ROOMID = rid
	url = 'https://hipchat.rbc.ru/v2/room/%d/history' % int(ROOMID)
	headers = {
	 "content-type": "application/json",
	 "authorization": "Bearer %s" % V2TOKEN}

	request = requests.get(url, headers=headers, verify=False)
	msg=json.loads(request.content)
	return msg["items"][-1]["message"]