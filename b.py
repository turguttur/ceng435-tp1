import socket
import sys
import time

# s: - Interface 0: "10.10.1.1"
# b  - Interface 1: "10.10.1.2"
# b  - Interface 2: "10.10.2.1"
# b  - Interface 6: "10.10.4.1"
# r1 - Interface 3: "10.10.2.2"
# r1 - Interface 4: "10.10.3.1"
# r2 - Interface 7: "10.10.4.2"
# r2 - Interface 8: "10.10.5.1"
# d  - Interface 5: "10.10.3.2"
# d  - Interface 9: "10.10.5.2"

# Interface 0: "10.10.1.1"
# Interface 1: "10.10.1.2"
# Interface 2: "10.10.2.1"
# Interface 3: "10.10.2.2"
# Interface 4: "10.10.3.1"
# Interface 5: "10.10.3.2"
# Interface 6: "10.10.4.1"
# Interface 7: "10.10.4.2"
# Interface 8: "10.10.5.1"
# Interface 9: "10.10.5.2"

ips = ["10.10.1.1",
	   "10.10.1.2",
	   "10.10.2.1",
	   "10.10.2.1",
	   "10.10.3.1",
	   "10.10.3.2",
	   "10.10.4.1",
	   "10.10.4.2",
	   "10.10.5.1",
	   "10.10.5.2"]

# Listen TCP connection from s with Interface 1

sockets = []
def InitializeConnections():
	host_s = ips[1]		# s ip
	port_s = 5000		
	sock_s = socket.socket()
	sock_s.bind((host_s, sock_s))
	sockets.append(sock_s)

	hostb_i2 = ips[2]
	portb_i2 = 8000
	r1 = (ips[3], 8001)
	sock_r1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock_r1.bind((hostb_i2, portb_i2))
	sockets.append(sock_r1)	
	

def TCPconnection():
	sockets[0].listen(1)
	c, addr = sockets[0].accept()
	print("Connection from: " + str(addr)) 
	while True:
		try:
			data = c.recv(1024)
			sockets[1].sendto(data, (ips[3], 8001))
			if not data:
				break
			print("From connected user: " + str(data))
		except:
			continue
	sockets[0].close()
	sockets[1].close()

def Main():
	InitializeConnections()
	TCPconnection()

if __name__ == "__main__":
	Main()
