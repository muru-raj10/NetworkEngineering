# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:06:42 2018

@author: User
"""

from socket import *
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#mailServer = 'smtp.gmail.com'#Fill in start   #Fill in end
mailServer = 'smtp.mail.yahoo.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start  
mailPort = 25
clientSocket = socket(AF_INET,SOCK_STREAM)
"""
clientSocket = ssl.wrap_socket(clientSocket,      #Here we try to create a secure socket to that
                ssl_version=ssl.PROTOCOL_TLSv1,     #the mail server makes a handshake and create the response
                ciphers="HIGH:-aNULL:-eNULL:-PSK:RC4-SHA:RC4-MD5",
                cert_reqs=ssl.CERT_REQUIRED)
"""
clientSocket.connect((mailServer, mailPort))
 
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
# Fill in start
mailfrom = 'MAIL FROM: <alice@crepes.fr>'
clientSocket.send(mailfrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Fill in end

# Send RCPT TO command and print server response. 
# Fill in start
rcptto = 'RCPT TO: <muru.raj10@google.com>'
clientSocket.send(rcptto.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response. 
# Fill in start
data = 'DATA'
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
clientSocket.send((msg).encode())
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send((endmsg).encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv4[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quite = 'QUIT'
clientSocket.send(quite.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')
# Fill in end

clientSocket.close()