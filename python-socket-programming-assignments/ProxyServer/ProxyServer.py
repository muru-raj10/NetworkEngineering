# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 17:46:10 2018

@author: User
"""
r"C:\Users\User\Desktop\Victoria\NWEN302 - Network Engineering (Seah)\python-socket-programming-assignments\ProxyServer"
from socket import *
import sys

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
	
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerPort=8888
serverip = sys.argv[1] #from argument
print(serverip)
tcpSerSock.bind((serverip, tcpSerPort))
tcpSerSock.listen(5)
# Fill in end.
while 1:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()  # Fill in start.		# Fill in end.
    #print(message)
    # Extract the filename from the given message
    #print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    try:
        f = open(filetouse[1:], "r") # Check wether the file exist in the cache
        outputdata = f.read()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")            
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in start.
        resp = ""
        for s in outputdata:
            resp+=s
        tcpCliSock.send(resp.encode())
		# Fill in end.
        print('Read from cache') 
	# Error handling for file not found in cache
    except IOError:
        if fileExist == "false": 
			# Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)# Fill in start.		# Fill in end.
            hostn = filename.replace("www.","",1)         
            print(hostn)                                  
            try:
				# Connect to the socket to port 80
				# Fill in start.
                c.connect((hostn,80))
              # Fill in end.
				# Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('rw')
                fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")  
                print('filewritten!')
                # Read the response into buffer
				# Fill in start.		
                resp = c.recv(4096)
                response = ""
                while resp:
                    print(resp)
                    response+=resp
                    resp = c.recv(4096)
				# Fill in end.
				# Create a new file in the cache for the requested file. 
				# Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename,"wb")  
				# Fill in start.		
                tmpFile.write(response)
                tmpFile.close()
              # Fill in end.			
            except:
                print("Illegal request")
                sys.exit(2)                                               
        else:
			# HTTP response message for file not found
			# Fill in start.		
            c.send('HTTP/1.0 404 Not Found\r\n'.encode())
            c.close()
          # Fill in end.
	# Close the client and the server sockets    
    tcpCliSock.close() 
# Fill in start.		
# Fill in end.
