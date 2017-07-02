#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
from operator import is_not
from functools import partial
from time import sleep

from tequila_classes import IO

cmdargs = sys.argv
#first arg is room id
room_id = 332
#just testing git branches


while True:
	bot = IO()
	#bot.test()
	bot.load("332",
			 "red",
			 "PX9ZwyIFnBsPaTW9xUbtMCaYenmJ0VwwNY5xG9j0",
			 "PX9ZwyIFnBsPaTW9xUbtMCaYenmJ0VwwNY5xG9j0",
			 "PX9ZwyIFnBsPaTW9xUbtMCaYenmJ0VwwNY5xG9j0",
			 "PX9ZwyIFnBsPaTW9xUbtMCaYenmJ0VwwNY5xG9j0",
			 "iderkun",
			 "K3k9hpfX@")
	key = bot.read()
	token=[		"tequila",   #0
				"!ping",     #1
				"!weather",  #2
				"!google",   #3
				"!host",     #4
				"!calc",     #5
				"!bot",		 #6
				"!help",	 #7
				"!info",	 #8
				"!hipcreate",#9
				"!invite",   #10
				"!jircreate", #11
				"!getproblems"
				]
	if token[0] in key:
		bot.tqla()
	elif token[1] in key:
		bot.ping(key)
	elif token[2] in key:
		bot.wthr()
	elif token[4] in key:
		bot.write("In progress...")
		bot.jcreate("lalala")
	elif token[5] in key:
		bot.calc(key)
	elif (token[6] in key) or (token[7] in key) or (token[8] in key):
		bot.hello()
	elif token[9] in key:
		bot.croom(key,"botmaded room")
	elif token[10] in key:
		bot.iuser(key)
	elif token [11] in key:
		bot.jcreate(key)
	elif token [12] in key:
		bot.gproblems(key)
	sleep (5)



