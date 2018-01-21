# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:37:33 2018

@author: User
"""

from socket import *
import time
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

counter = 1

while counter < 11 :
    counter+=1
    currentTime=time.localtime()
    #build ping message and send and wait 1 s
    msg = 'Ping {} {}'.format(counter,currentTime)
    clientSocket.sendto(pingMessage, ('localhost',12000))
    clientSocket.settimeout(1)
    
    try:
		messageReturn,serverAddress = clientSocket.recvfrom(1024)
		# Print out the returned message (I am a ping) in all caps
		print messageReturn
		# Get current time minus start time for the RTT
		rtt = (time.time()-start)
		# Print out the RTT
		print('RTT: {}\n\n'.format(rtt))

	# If there is a timeout print request timed out
	except timeout:
		print('Request timed out\n\n')
        
#Close the socket
clientSocket.close()

    
