# chat server
'''
chat server must perform two functions:
	1. accept multiple incoming connections from clients
	2. read all incoming messages and broadcast to all connected clients

'''
import socket #for sockets
import select #for multiplexing

# broadcast function - broadcasts message to all connected clients
def broadcast_msg(client_sock, msg):
	# master socket: defined as the server socket
	# don't send to master socket nor the sending cliet socket
	for socket in CONNECTION_LIST:
		if socket != server_socket and socket != client_sock:
			try:
				socket.send(msg)

			except:
				# if the send fails, that client is assumed dead and connection is closed
				socket.close()
				CONNECTION_LIST.remove(socket) # remove dead client from 'chat party'

if __name__ == "__main__":

	# list to identify all socket descriptors
	CONNECTION_LIST = []
	recv_buff = 4096
	PORT = 5000

	# create server socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# AF_INET: address type: IPv4
	# SOCK_STREAM: socekt type: TCP
	# ensure that the socket can be resuesed while in the 'wait state' (multiple connections)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# bind socket to port/address
	server_socket.bind(('', PORT))
	server_socket.listen(10) #listen for connections, keep 10 connections in wait queue

	# add the server socket to list of readable sockets connections
	CONNECTION_LIST.append(server_socket)

	print 'Chat server started on port ' + str(PORT)

	# service connections and client requests
	while True:
		# keep alive

		# get list of all sockets that can be read
		read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [],[])

		for sock in read_sockets:
			if sock == server_socket:
				# new connection - handle case of a new incoming client connection on server_socket
				new_client_sock, addr = server_socket.accept()
				CONNECTION_LIST.append(new_client_sock)
				print 'Client (%s, %s) connected' % addr

				# broadcast the connection message of new client joining the chat party
				broadcast_msg(new_client_sock, ('[%s:%s] entered the room\n' % addr))

			else:
				# not a new client, but a message from an existing client
				# message to be broadcasted to all in chat room
				try:
					# get data from client socket
					data_from_client = sock.recv(recv_buff)
					if data_from_client:
						# broadcast the message to all other clients
						broadcast_msg(sock, '\r' + '<' + str(sock.getpeername()) + '>' + data_from_client)

				except:
					# if fails
					broadcast_msg(sock, ("Client (%s, %s) is offline" % addr))
					print "Client (%s, %s) is offline" % addr
					#close the client socket
					sock.close()
					#remove dead client from connection list
					CONNECTION_LIST.remove(sock)
					continue
	# eventually close the socket
	server_socket.close()
# use dictionary matching IP to hostnames?




