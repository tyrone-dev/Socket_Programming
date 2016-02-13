# chat client

'''
Chat client must do the following:
	1. listen for incoming messages from the server
	2. check for user input (i.e. messages to be sent to server)
	(simultaneously)
'''
import socket # for sockets
import select # to monitor sockets and file descriptors simultaneously
			  # to check for some activity
import string
import sys # for stdin (input) file descriptor
from datetime import datetime

def prompt():
	# function to display client's own text to terminal
	now = datetime.now()
	time = "%s:%s:%s" % (now.hour, now.minute, now.second)
	sys.stdout.write(time)
	sys.stdout.write('<You> ')
	sys.stdout.flush()

if __name__ == "__main__":
	if(len(sys.argv) < 3):
		# not enough arguments for executing script
		print "Usage: python chat_server.py hostname port"
		sys.exit()

	# get hostname and port (of server) from exc args
	host = sys.argv[1]
	port = int(sys.argv[2])

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.settimeout(2)

	# connect to the remote host (chat server)
	try:
		client_socket.connect((host,port))
	except:
		print "Unable to connect to remote host"
		sys.exit()

	print "Connect to Chat Sever. Start sending messages :)"
	prompt()

	# check for user input or incoming messages
	while True:
		socket_list = [sys.stdin, client_socket]

		# use select to monitor activity on all descriptors
		# check which is readable
		read_sockets, write_sockets, error_sockets = select.select(socket_list,[],[])

		for sock in read_sockets:
			# service incoming messages from server (comes in on client socket)
			if sock == client_socket:
				data = client_socket.recv(4096)
				if not data:
					print "\nDisconnected from chat server"
					sys.exit()
				else:
					#print data to terminal
					sys.stdout.write(data)
					prompt()
			else:
				# service user entered message - to be sent to server
				msg = sys.stdin.readline() #capture input
				client_socket.send(msg) # send to server
				prompt()

	# eventually close socket
	client_socket.close()
	# after connect with server send hostname


