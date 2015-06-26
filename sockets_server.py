# server socket activity

import socket
import sys
from thread import * #threads are used to handle multiple connection on the server

HOST = '' # Symbolic name to reference all available interfaces
PORT = 8888 # arbitary non-privledged port

my_serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socekt Created'

# bind the socket to a particular address & port

try: 
	my_serv_socket.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code: ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

# make the binded socket listen for connections
# binding to a port and ip ensures all incoming data directed to this port/ip combo is captured by program

# put the socket in 'listening' mode
my_serv_socket.listen(10) # paramater: backlog, specifies number of incoming connection that are kept waiting if program is busy
print 'Socket is now listening' 

# function for handling connection. This creates threads
def client_thread(conn):
	#send message to client
	conn.send('Welcome to the server. Type something and hit enter\n') #send only works on strings
	
	# inf loop to prevent func from terminate and keep thread alive
	while True:
		
		# recv data from client
		data = conn.recv(1024)
		reply = 'OK...' + data
		if not data:
			break

		conn.sendall(reply) #send reply to client
		
	# when loop broken
	conn.close()

# accept connections
# live server
while True:
	# wait to accept a connection - blocking call
	conn, addr = my_serv_socket.accept()

	# display client information
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

	#start a new thread: 1st arg is the name of the function to be threaded, 2nd arg is tuple (, , ,) of args to function
	start_new_thread(client_thread, (conn,))

# close socket
my_serv_socket.close()	
