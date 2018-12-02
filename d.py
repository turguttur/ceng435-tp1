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
		t = int(time.time() * 1000)
		e2e = t - int(data[15:28])
		print data + " with E2E: " + str(e2e)
		print "END TIME: ", str(t)
	 	ACK = "ACK(" + str(t) + "):" + data[:13]
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
	 	t = int(time.time() * 1000)
	 	e2e = t - int(data[15:28])
		print data + " with E2E: " + str(e2e)
		print "END TIME: ", str(t)
	 	ACK = "ACK(" + str(t) + "):" + data[:13]
	 	s.sendto(ACK, ("10.10.5.1", 8001))
	s.close()

def Main():
	thread1 = threading.Thread(target = ListenR1, args=())
	thread2 = threading.Thread(target = ListenR2, args=())
	thread1.start()
	thread2.start()

if __name__ == '__main__':
	Main()