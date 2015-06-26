# socket programming tutorial: TCP sockets

import socket #to use sockets
import sys #for system calls like exit



try:
        # create socket: AF_INET     : IPv4 [Adress family]
        #		 SOCK_STREAM : TCP [Type]
	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates socket and returns a socket descriptor (can be sued for other socket functions)

except socket.error, msg:
	# socket.error is the exception thrown, msg is the name we give it
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	sys.exit()

print "Socket created" 

# connect to server

host = 'www.google.com'
port = 80

try:
	remote_ip = socket.gethostbyname( host )
	# get ip address of host by name
except socket.gaierror:
	#could not resolve
	print "Hostname could not be resolved. Exiting"
	sys.exit()
	
print 'IP address of ' + host + ' is ' + remote_ip

# connect to the remote server using IP address and port

my_socket.connect((remote_ip, port))


print 'Socket Connected to ' + host + ' on IP: ' + remote_ip

# send data to the remote server 
message = "GET / HTTP/1.1\r\n\r\n" # HTTP GET message to fetch the mainpage

try :
	#send whole string
	my_socket.sendall(message)
except socket.error:
	#send failed
	print "Send Failed"
	sys.exit

print 'Message sent successfully'

# receieve the respone from the server
reply_from_server = my_socket.recv(4096)

print reply_from_server

# close the socket after comms

my_socket.close()
