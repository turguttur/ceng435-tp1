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

def Main():
	# s with Interface 0 to b with Interface 1
	host = ips[1]	# b's Interface 1 ip address
	port = 9000		# The port used by b's Interface 1

	s = socket.socket()
	s.connect((host, port))
	for msg in range(100, 200):
		s.send(str(msg))
		print("PACKET->" + str(msg) + " sent", flush = True)
	s.close()

if __name__ == "__main__":
	Main()

