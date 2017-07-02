#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
def state(host):
	hostname = host
	response = os.system("ping -c 5 " + hostname)

	#and then check the response...
	if response == 0:
	  return "%s is up!" % hostname
	else:
	  return "%s is down!" % hostname