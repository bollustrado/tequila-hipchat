#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
def get_owner_on_host(host):
	clear_owner_array=[]
	conn= psycopg2.connect("user='kds' host='devel.kds.corp.hostcomm.ru' port='8888' password='0000ABCDFF'")
	curs=conn.cursor()
	curs.execute("select resp_uids from hosts where name = "+host)
	owner_array=curs.fetchall()

	for owner in owner_array:
       		clear_owner_array.append(str(owner).replace(",",""))

	
	return clear_owner_array

print get_owner_on_host("'ns8-4.nic.ru'") #Передавать именно в таком формате !("'value'")!, иначе библиотека не сомжет осуществить поиск из-за точки в названии
