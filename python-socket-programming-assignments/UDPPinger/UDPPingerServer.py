# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:35:01 2018

@author: User
"""

# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
import time
from socket import *

import pickle

class ProcessData:
    counter = 0
    currentTime = time.struct_time
    
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
timelist = []

while True:
	# Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)    
    # Receive the client packet along with the address it is coming from 
    data, address = serverSocket.recvfrom(1024)
    var=pickle.loads(data)
    timelist.append(var.currentTime)
    if len(timelist)==2:
        timetaken = time.mktime(timelist[1])-time.mktime(timelist[0])
        timelist.pop()
        timelist.pop()
	# Capitalize the message from the client
    timestr = '{}'.format(var.currentTime)
    message = timestr.upper()
	# If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
	# Otherwise, the server responds    
    #serverSocket.sendto(message, address)
    serverSocket.sendto(message.encode(), address)