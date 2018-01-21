# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:15:25 2018

@author: User
"""

#import socket module
from socket import *
import sys # In order to terminate the program
import os 
print(os.getcwd())

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort=6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
#192.168.1.88:6789
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  #Fill in start             #Fill in end          
    print(addr)
    try:
        message = connectionSocket.recv(1024).decode() #Fill in start         #Fill in end               
        filename = message.split()[1]
        f = open(filename[1:])                        
        outputdata = f.readlines() #Fill in start       #Fill in end                
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode())
        #Fill in end                
        #Send the content of the requested file to the client
        resp=""
        for i in range(0, len(outputdata)):
            resp+=outputdata[i]
        connectionSocket.send(f)
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
        
    except IOError:
        #Send response message for file not found
        #Fill in start    
        connectionSocket.send('HTTP/1.0 404 Not Found\r\n'.encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end            
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
#C:\Users\User\Documents\HTML\2-html\new-zealand.html