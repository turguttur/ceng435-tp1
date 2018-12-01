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


def Main():
	host = "10.10.2.2"
	port = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	for i in range(0, 100):
		data, addr = s.recvfrom(1024)
		print data
		s.sendto("ACK", ("10.10.2.1", 8001))
	s.close()

if __name__ == '__main__':
	Main()