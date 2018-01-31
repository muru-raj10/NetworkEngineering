# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:15:25 2018

@author: User
"""

#import socket module
from socket import *
import sys # In order to terminate the program
import os 
#print(os.getcwd())

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverHost = "10.62.1.35"
serverPort=6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    #Establish the connection
    print('Ready to serve...')
    (connectionSocket, addr) = serverSocket.accept()         
    print(addr)
    try:
        message = connectionSocket.recv(1024).decode() 
        #print(message)             
        filename = message.split()[1]
        f = open(filename[1:])                        
        outputdata = f.readlines()   
        #print(outputdata)            
        #Send one HTTP header line into socket
        connectionSocket.send(('HTTP/1.0 200 OK\r\n').encode())
                        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
           connectionSocket.send((outputdata[i]).encode())
        #connectionSocket.send("""
        #                      <html>
        #                      <body>
        #                      <h1> Hello World!</h1>
        #                      I am finally here!
        #                      </body>
        #                      </html>
        #                      """.encode())
        
        connectionSocket.send(("\r\n").encode())
        
        connectionSocket.close()
        
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.0 404 Not Found\r\n'.encode())
        #Close client socket
        connectionSocket.close()
    except IndexError:
        pass #remain listening
                    
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 

#http://ipaddress:6789/new-zealand.html