import socket

port = 5000

# create udp socket
my_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# AF_INT: Address Family: IPv4
# SOCK_DGRAM: Socket Type: UDP
my_udp_sock.bind(("",port))
print "waiting on port:", port
while True:
	data, addr = my_udp_sock.recvfrom(1024)
	print data

