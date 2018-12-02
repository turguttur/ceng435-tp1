import socket
import time
import threading

def ListenR1():
	host = "10.10.3.2"
	port = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	while True:
		data, addr = s.recvfrom(1024)
		if not data:
			break
		print data
		ACK = "ACK " + data[:13]
		s.sendto(ACK, ("10.10.3.1", 8001))
	s.close()

def ListenR2():
	host = "10.10.5.2"
	port = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	while True:
	 	data, addr = s.recvfrom(1024)
	 	if not data:
	 		break
	 	print data
	 	ACK = "ACK " + data[:13]
	 	s.sendto(ACK, ("10.10.5.1", 8001))
	s.close()

def Main():
	th = threading.Thread(target = ListenR1, args=())
	th2 = threading.Thread(target = ListenR2, args=())
	th.start()
	th2.start()

if __name__ == '__main__':
	Main()