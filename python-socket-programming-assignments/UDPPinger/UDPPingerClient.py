# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:37:33 2018

@author: User
"""

from socket import *
from numpy import mean
import time
import pickle

class ProcessData:
    def __init__(self,counter,currentTime):
        self.counter = counter
        self.currentTime = currentTime

# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

var = ProcessData(counter=1,currentTime=time.localtime())
rttlist=[]
loss=0
while var.counter < 11 :
    var.counter+=1
    var.currentTime=time.localtime()
    starttime = time.time()
    #build ping message and send and wait 1 s
    pingMessage = pickle.dumps(var)
    #clientSocket.sendto(pingMessage.encode(), ('localhost',12000))
    clientSocket.sendto(pingMessage, ('localhost',12000))
    clientSocket.settimeout(1)

    try:
        messageReturn,serverAddress = clientSocket.recvfrom(1024)
		# Print out the returned message (I am a ping) in all caps
        print(messageReturn)
		# Get current time minus start time for the RTT
        rtt = (time.time()-starttime)
        rttlist.append(rtt)
		# Print out the RTT
        print('RTT: {}\n\n'.format(rtt))

	# If there is a timeout print request timed out
    except timeout:
        print('Request timed out\n\n')
        loss+=1
maxrtt = max(rttlist)
minrtt = min(rttlist)
avrtt = mean(rttlist)
lossrate = loss/10.0 * 100
print('rtt: maximum={}, minumum={}, average={}'.format(maxrtt,minrtt,avrtt))
print('packet loss rate:{}%'.format(lossrate))
#Close the socket
clientSocket.close()

    
