import socket
import sys
import time
from random import randint

# s  (interface-0): "10.10.1.1"
# b  (interface-1): "10.10.1.2"
# b  (interface-2): "10.10.2.1"
# b  (interface-6): "10.10.4.1"
# r1 (interface-3): "10.10.2.2"
# r1 (interface-4): "10.10.3.1"
# r2 (interface-7): "10.10.4.2"
# r2 (interface-8): "10.10.5.1"
# d  (interface-5): "10.10.3.2"
# d  (interface-9): "10.10.5.2"

def TCP2UDP(message, pathFlag, routerDict):
	host = (routerDict[pathFlag])[0]
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((routerDict[pathFlag])[1])
	message += "->b"
	s.sendto(message, host)
	data, addr = s.recvfrom(1024)
	s.close()
	return data

'''
	if pathFlag == 'r2':
		host = "10.10.4.2"		# R2 (interface-7) link-4 endpoint#1
 		port = 8000				# R2 interface-7 port
 		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 		s.bind(("10.10.4.1", 8002))
 		message += "->r2"
 		s.sendto(message, (host, port))
 		data, addr = s.recvfrom(1024)
 		s.close()
 		return data, 'r1'
	else:	
		host = "10.10.2.2" 		# R1 (inteface-3) link-1 endpoint#1
		port = 8000
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind(("10.10.2.1", 8001))
		message += "->r1"
		s.sendto(message, (host, port))
		data, addr = s.recvfrom(1024)
		s.close()
		return data, 'r2'
'''

def Main():
	host = "10.10.1.2"
	port = 8000
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, addr = s.accept()
	
	routerDict = {
		1: [("10.10.2.2", 8000), ("10.10.2.1", 8001)],
		2: [("10.10.4.2", 8000), ("10.10.4.1", 8002)]
	}

	for i in range(0, 2500):
		message = c.recv(1024)
		if not message:
			break
		print "RECEIVED MESSAGE: " + message
		pathFlag = randint(1, 2)
		data = TCP2UDP(message, pathFlag, routerDict)
		ACK = data + "->b"
		#ack = "ACK" + '{0:04}'.format(i)
		c.send(ACK)

if __name__ == "__main__":
	Main()
