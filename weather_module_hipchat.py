#!/usr/bin/env python

import os
import json
import requests
import datetime
def get():
        date = datetime.datetime.now()
        date = date.isoformat()
        api_key = 'e68c430c0f52cfb39e482886c2a536ed' #my API token on developer.forecast.io
        lat = 55.7742 #Moscow NIC office
        lng = 37.4731
        url = "https://api.forecast.io/forecast/%s/%s,%s" % (api_key, lat, lng)
        request = requests.get(url).json()
        return (request["daily"]["summary"]).encode('utf-8')
