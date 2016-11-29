#!/usr/bin/env python

# https://eclipse.googlesource.com/paho/org.eclipse.paho.mqtt.python/+/1.1/examples
import re
import paho.mqtt.client as mqtt
fd = open('document.csv','a')

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("IOT/")

def on_message(client, userdata, msg):
	if msg.payload != '' :
		print(msg.payload)
		fd.write(msg.payload)

client = mqtt.Client()
client.connect("10.84.45.126",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
fd.close()