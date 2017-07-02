import json
import ssl
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def writethis(text,rid,token_id, color):
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	# API V2, send message to room:
	url = 'https://hipchat.rbc.ru/v2/room/%d/notification' % int(rid)
	message = text
	headers = {
    "content-type": "application/json",
    "authorization": "Bearer %s" % token_id}
	datastr = json.dumps({
    'message': message,
    'color': color,
    'message_format': 'html',
    'notify': False})
	request = requests.post(url, headers=headers, data=datastr, verify=False)
	return request
