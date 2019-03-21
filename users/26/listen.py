import socket
import time
import datetime
import os
import sys

UDP_IP = "localhost"
UDP_PORT = 5000

def getline():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data,addr=sock.recvfrom(1024)
        return data
    sock.close()



if __name__ == "__main__":
	first=0
	f=open("data.dat", 'w')
	while True:
		l=(getline())
		if l:
			if first==0:
				st=datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%S.%f")
				print("Started at", st)
				os.system("echo %s > data_start_time.txt" %(st))
				first=1
			l=str(l, 'utf-8')
			print(l)
			f.write(l)
			f.flush()
