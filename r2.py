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

def Route(message):
	host = "10.10.5.2"
	port = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(("10.10.5.1", 8001))
	message += "->r2"
	s.sendto(message, (host, port))
	data, addr = s.recvfrom(1024)
	s.close()
	return data

def Main():
	host = "10.10.4.2"
	port = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	while True:
		data, addr = s.recvfrom(1024)
		if not data:
			break
		print data
		ACK = Route(data)
		ACK += "->r2"
		s.sendto(ACK, ("10.10.4.1", 8002))
	s.close()		

if __name__ == '__main__':
	Main()