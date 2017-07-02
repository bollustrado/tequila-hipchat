#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import read_module_hipchat as read
import write_module_hipchat as write
import calc_module_hipchat as calc
import ping_module_hipchat as ping
import weather_module_hipchat as weather
import tequila_module_hipchat as tequila
import createroom_module_hipchat as create
import user_module_hipchat as user
import create_jira_module as icreate
import monitoring_module as monitor

class IO:
	r_id  =""  #Room ID
	color =""  #Color of text
	w_tid =""  #Write token
	r_tid =""  #Read token
	c_tid =""  #Create room ID
	j_log =""  #Jira login
	j_pas =""  #Jira pass
	def load(self, room_id, write_color,
	         write_token, read_token,
	         creater_token, user_token, jira_login,jira_password):
		self.r_id = room_id
		self.w_tid = write_token
		self.r_tid = read_token
		self.cr_tid = creater_token
		self.iu_tid = user_token
		self.color = write_color
		self.j_log = jira_login
		self.j_pas = jira_password
	def read(self):
		return read.getlast(self.r_id,self.r_tid)
	def write(self, data):
		write.writethis(data, self.r_id, self.w_tid, self.color)
	def calc(self,data):
		write.writethis(str(rez), self.r_id, self.w_tid, self.color)
	def tqla(self):
		write.writethis(tequila.getfact(), self.r_id, self.w_tid, self.color)
	def ping(self, data):
		write.writethis((str(ping.state(data.replace("!ping", "")))), self.r_id, self.w_tid, self.color) #TODO: по-хорошему нужно инкапсулировать обрезалку пингов внутрь
	def wthr(self):
		write.writethis(str(weather.get()), self.r_id, self.w_tid, self.color)
	def hello(self):
		write.writethis(str(tequila.hello()), self.r_id, self.w_tid, self.color)
	def croom(self,rname,rtopic):
		croom_id=create.new(rname,rtopic,self.cr_tid)
		write.writethis("Created new room. ID %s: " % str(croom_id), self.r_id, self.w_tid, self.color)
	def iuser(self,rid_uid):
		info=user.invite(rid_uid,self.iu_tid)
		write.writethis(str(info), self.r_id, self.w_tid, self.color)
	def jcreate(self,data):
		icreate.newissue(self.j_log, self.j_pas, data)
		write.writethis(str("stopme"), self.r_id, self.w_tid, self.color)
	def gproblems(self, data):
		monitor.getproblems("pohui","hardcoded", data.split()[-1])
		write.writethis(str("stopme"), self.r_id, self.w_tid, self.color)

		