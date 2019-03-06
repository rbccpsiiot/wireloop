import socket


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
    while True: print(getline())
        
