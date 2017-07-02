#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def solve(sub_input):
	# input is a list of tokens (token is a number or operator)

	tokens = (re.sub("[^0-9,*+-//]", "", sub_input))
	#rez=calc.solve(re.sub("[^0-9,*+-//]", "", data))

	pattern = re.compile("^([0-9]+)*$")
	if pattern.match(tokens):
		return "go fuck yourself, scriptkiddy"

	# remove whitespace
	tokens = re.sub('\s+', '', tokens)

	# split by addition/subtraction operators
	tokens = re.split('(-|\+)', tokens)

	# takes in a string of numbers, *s, and /s. returns the result
	def solve_term(tokens):
	    tokens = re.split('(/|\*)', tokens)
	    ret = float(tokens[0])
	    for op, num in zip(tokens[1::2], tokens[2::2]):
	        num = float(num)
	        if op == '*':
	            ret *= num
	        else:
	            ret /= num
	    return ret

	# initialize final result to the first term's value
	result = solve_term(tokens[0])

	# calculate the final result by adding/subtracting terms
	for op, num in zip(tokens[1::2], tokens[2::2]):
	    result +=  solve_term(num) * (1 if op == '+' else -1)

	return result