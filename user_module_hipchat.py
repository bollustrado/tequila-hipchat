#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import ssl
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def invite(rid_uid,tid):
    rid_uid =rid_uid.replace("!invite", "").encode('utf-8')
    rid_uid_splitted  = rid_uid.split(' ')
    rid = rid_uid_splitted[1]
    uid = rid_uid_splitted[2]
    print  "Room ID: %s" %rid
    print  "User ID: %s" %uid
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = 'https://hipchat.rbc.ru/v2/room/%s/invite/%s' % (rid,uid)
    headers = {
    "content-type": "application/json",
    "authorization": "Bearer %s" % tid}
    request = requests.post(url, headers=headers, verify=False)
    try:
        msg=json.loads(request.content)
        return msg
    except:
        return "%s is invited to room #%s" % (uid,rid)