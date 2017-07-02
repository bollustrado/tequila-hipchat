#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
list_project_host={"GETLIST":"select host,service,status_info,duration from services_problems where status='CRITICAL'",
						"GETUNIQHOST":"select distinct host from services_problems where status='CRITICAL'",
					   "CORE":"select * from hosts where resp_uids ~'ddubrovin' and status='CRITICAL'",
					   "NIC":"select * from hosts where resp_uids~'obravo' and status='CRITICAL'",
					   "HC":"select * from hosts where resp_uids~'szapuskalov' and status='CRITICAL'"}

conn= psycopg2.connect("user='kds' host='devel.kds.corp.hostcomm.ru' port='8888' password='0000ABCDFF'")
curs= conn.cursor()
curs.execute(list_project_host['GETLIST'])
all_problems=curs.fetchall()

#Получаем уникальные значения хостов, в целях сортировки и получения в конечно итоге массив-хост и тому подобное
curs= conn.cursor()
curs.execute(list_project_host['GETUNIQHOST'])
uniq_host=curs.fetchall()

number=0
clear_uniq_host=[]

for item_uniq_host in uniq_host:
	clear_uniq_host.append(str(item_uniq_host).replace(",",""))

while number < len(clear_uniq_host):
	try:
		print clear_uniq_host[number]
		curs.execute("select * from services_problems where host ~ "+str(clear_uniq_host[number]))
		value=curs.fetchall()
		print value
		number +=1
	except IndexError:
		break

