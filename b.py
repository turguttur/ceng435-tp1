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
# 

def Main():
	host = ips[1]	# Listen TCP connection from s with this inteface
	port = 9000 	# Listen TCP connection from s with this port

	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, addr = s.accept()
	print("Connection from: " + str(addr), flush = True)
	while True:
		try:
			data = c.recv(1024)
			if not data:
				break
			print("from connected user: " + str(data), flush = True)
			sleep(0.1)
		except:
			continue
	s.close()

if __name__ == "__main__":
	Main()
