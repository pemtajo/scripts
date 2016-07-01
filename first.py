#!/usr/bin/python

import socket
ip = raw_input("Enter the IP filha da puta: ")
port =  input("Enter o numero da porta caralho: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sock.connect_ex((ip,port)):
	print "Port ", port, " is closed"
else:
	print "Port ",port , " esta aberta porraaa!!"

