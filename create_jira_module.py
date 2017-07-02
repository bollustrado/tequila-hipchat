#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re  
reload(sys)  
sys.setdefaultencoding('utf-8')

from jira import JIRA

def newissue(login,passw,data):

	data=data.replace("!jircreate ", "")
	data_s=data.split(';')
	proj = data_s[0]
	itype= data_s[1]
	print itype;
	summ = data_s[2]
	desc = data_s[3]
	options = {
	    'server': 'https://jira.rbc.ru',
	    'verify': False
	}
	jira = JIRA(options, basic_auth=(login, passw))
	new_issue = jira.create_issue(project=proj,
								  summary=summ,
	                              description=desc,
	                              issuetype={'name': itype})