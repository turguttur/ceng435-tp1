import socket
import sys
import time

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

def TCP2UDP(message):
	host = "10.10.4.2"		# R2 (interface-7) link-4 endpoint#1
	port = 8000				# R2 interface-7 port
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(("10.10.4.1", 8002))
	message += "->r2"
	s.sendto(message, (host, port))
	data, addr = s.recvfrom(1024)
	s.close()
	return data

def TCP2UDP(message, pathFlag):
	if pathFlag == 'r1':
		host = "10.10.2.2" 		# R1 (inteface-3) link-1 endpoint#1
		port = 8000
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind(("10.10.2.1", 8001))
		message += "->r1"
		s.sendto(message, (host, port))
		data, addr = s.recvfrom(1024)
		s.close()
		return data, 'r2'
	else:
		host = "10.10.4.2"		# R2 (interface-7) link-4 endpoint#1
 		port = 8000				# R2 interface-7 port
 		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 		s.bind(("10.10.4.1", 8002))
 		message += "->r2"
 		s.sendto(message, (host, port))
 		data, addr = s.recvfrom(1024)
 		s.close()
 		return data, 'r1'

def Main():
	host = "10.10.1.2"
	port = 8000
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, addr = s.accept()
	pathFlag = 'r1'
	for i in range(0, 100):
		message = c.recv(1024)
		if not message:
			break
		data = TCP2UDP(message)
		print "Received: " + data
		ack = "ACK" + '{0:04}'.format(i)
		c.send(ack)

if __name__ == "__main__":
	Main()
