#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
#CORE+ HC+ NIC+ 

#Active services
#kds=> \d services_problems;
#              Table "public.services_problems"
#    Column    |            Type             |   Modifiers   
#--------------+-----------------------------+---------------
# host         | text                        | not null
# service      | text                        | not null
# status       | text                        | 
# duration     | bigint                      | 
# last_check   | text                        | 
# attempt      | text                        | 
# status_info  | text                        | 
# ctime        | timestamp without time zone | default now()
# mtime        | timestamp without time zone | default now()
# has_comments | boolean                     | default false
# sd           | boolean                     | default false
# ack          | boolean                     | default false
# fresh        | boolean                     | default true
#kds=> \d hosts;
#                      Table "public.hosts"
#      Column      |            Type             |   Modifiers   
#------------------+-----------------------------+---------------
# name             | text                        | not null
# extra_notes_orig | text                        | 
# extra_notes      | text                        | 
# resp_uids        | text                        | 
# watch_time       | integer                     | 
# mby              | text                        | 
# ctime            | timestamp without time zone | default now()
# mtime            | timestamp without time zone | default now()
# internal_notes   | text                        | 
# important        | integer                     | default 0
# tmp_nic          | integer                     | default 0
# tmp_project      | text                        | 

def getproblems(login,passw,project):

	list_project_host={"GETLIST":"select host,service,status_info,duration from services_problems where statu='CRITICAL' order by duration",
					   "CORE":"select * from hosts where resp_uids ~'ddubrovin'",
					   "NIC":"select * from hosts where resp_uids~'obravo'",
					   "HC":"select * from hosts where resp_uids~'szapuskalov'"}

	conn= psycopg2.connect("user='kds' host='devel.kds.corp.hostcomm.ru' port='8888' password='0000ABCDFF'")
	curs= conn.cursor()
	curs.execute(list_project_host['GETLIST'])
	all_problems=curs.fetchall()
	#conn= psycopg2.connect("user='kds' host='devel.kds.corp.hostcomm.ru' port='8888' password='0000ABCDFF'")
	#curs= conn.cursor()
	#curs.execute(list_project_host[project])
	#owner_and_hos=curs.fetchall()
	problist = {'count':0,'hostname':'','problem':'','problem_info':'','time':''}
	sizeoflist=0
	for prob in all_problems:
		#for host in owner_and_hos:
			#if host[0]==prob[0]:
				problist[sizeoflist] = {'count':0,'hostname': prob[0],'problem': prob[1],'problem_info': prob[2],'time': prob[3]}
				#print project+" "+ prob[0]+"-"+prob[1]+"-"+prob[2]+" time:"+str(prob[3]) + "\n"
				sizeoflist+=1
	for x in range(1, sizeoflist):
		for y in range(0,sizeoflist):
			if problist[x]['hostname'] == problist[y]['hostname']:
				print x
		print problist[x]
		print "\n"


