# UDP client

import socket
import sys

# create UDP socket
try:
	my_udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg:
	print 'Failed to create socket'
	sys.exit()

host = 'localhost'
port = 8888

while True:
	msg = raw_input('Enter message to send: ')

	try:
		#send whole string
		my_udp_s.sendto(msg, (host,port))

		#receive data from client
		data, address = my_udp_s.recvfrom(1024)
		
		print 'Server reply : ' + data
	
	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        	sys.exit()
