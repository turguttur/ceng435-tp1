import socket
import time
import threading
import os
import csv

e2e_delay = []
def ListenR1():
	host = "10.10.3.2"
	port = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	while True:
		data, addr = s.recvfrom(1024)
		if not data:
			break
		rectime = time.time()
		#t = int(time.time() * 1000)
		e2e = int(rectime * 1000) - int(data[15:28])
		e2e_delay.append(e2e)
		print data + " with E2E: " + str(e2e)
	 	ACK = "ACK(" + str(int(rectime * 1000)) + "):" + data[:13]
		s.sendto(ACK, ("10.10.3.1", 8001))
		if data[8:12] == "2499":
	 		with open("e2e.csv", "wb") as csvfile:
	 			patcher = csv.writer(csvfile, dialect='excel')
	 			patcher.writerow(e2e_delay)
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
	 	rectime = time.time()
		#t = int(time.time() * 1000)
		e2e = int(rectime * 1000) - int(data[15:28])
		e2e_delay.append(e2e)
		print data + " with E2E: " + str(e2e)
	 	ACK = "ACK(" + str(int(rectime * 1000)) + "):" + data[:13]
	 	s.sendto(ACK, ("10.10.5.1", 8001))
	 	if data[8:12] == "2499":
	 		with open("e2e.csv", "wb") as csvfile:
	 			patcher = csv.writer(csvfile, dialect='excel')
	 			patcher.writerow(e2e_delay)
	s.close()

def Main():
	thread1 = threading.Thread(target = ListenR1, args=())
	thread2 = threading.Thread(target = ListenR2, args=())
	thread1.start()
	thread2.start()

if __name__ == '__main__':
	Main()