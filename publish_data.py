#!/usr/bin/env python
from flask import Flask, url_for , jsonify
import os
import datetime
import json
import re
import time
import paho.mqtt.publish as publish	
import sys
import StringIO as io
import os
import numpy as np
import pandas as pd 
import subprocess
reload(sys)
sys.setdefaultencoding('utf-8')

# https://eclipse.googlesource.com/paho/org.eclipse.paho.mqtt.python/+/1.1/examples

def restart_service(name):
    command = 'service ' + name  + ' restart'
    #shell=FALSE for sudo to work.
    subprocess.call(command, shell=False)

def transformation(data):
	donnees2 = data.replace(']', '')
	donnees = donnees2.replace('[', '')
	don = donnees[:-4]
	return(don)

def follow(name):
	current = open(name, "r")
	curino = os.fstat(current.fileno()).st_ino
	while True:
		while True:
			line = current.readline()
			line.encode('utf-8')
			if 'Notification' in line and '{' in line and '}':
				data = line.split(" ")
				date = data[0] + " "+ data[1]
				date = transformation(date)
				date_object = datetime.datetime.strptime(date , '%Y-%m-%d %H:%M:%S')
				test = line[line.find("{")+1:line.find("}")]
				toto = test.replace("\"", "'")
				test = toto.replace('\'', '"')
				test = "{"+test +"}"
				struct = json.loads(test)
				line=date + ';' + struct['dev'] + ';'+struct['l'] + '\n'
				fd.write(line)
				#msgs = [{'topic':"IOT/", 'payload':line}]
				#publish.multiple(msgs, hostname="10.84.45.126")
			if not line:
				break
			yield line
		try:
			if os.stat(name).st_ino != curino:
				new = open(name, "r")
				current.close()
				current = new
				curino = os.fstat(current.fileno()).st_ino
				continue
		except IOError:
			pass
		time.sleep(1)

if __name__ == '__main__':
	fd = open('document.csv','a')
	fname = '/var/log/z-way-server.log'
	os.remove(fname)
	open(fname,'a').close()
	restart_service('z-way-server')
	time.sleep(15)
	for l in follow(fname):
		pass
