import socket
import sys
PORT = 8888 
HOST = ''

try :
	 # create udp socket
	my_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	# AF_INT: Address Family: IPv4
	# SOCK_DGRAM: Socket Type: UDP
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    	sys.exit()
 
 
# Bind socket to local host and port
try:
	my_udp_sock.bind((HOST, PORT))
except socket.error , msg:
    	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    	sys.exit()
     
print 'Socket bind complete'
 
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    	data, addr = my_udp_sock.recvfrom(1024)
         
    	if not data: 
        	break
     
    	reply = 'OK...' + data
     
    	my_udp_sock.sendto(reply , addr)
    	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
     
my_udp_sock.close()
