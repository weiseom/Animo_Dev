# Echo client program
import socket

HOST = '52.78.63.210'                # The remote host
PORT = 5007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall('Hello, world')

while 1:
	data = s.recv(1024)
	if not data:break
	print 'Received', repr(data)

s.close()

