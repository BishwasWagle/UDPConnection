
import socket

def Main():
	host = '127.0.0.1'
	port = 5050

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	print("Server Started")

	while True:
		data = s.recvfrom(1024).decode('utf-8')
		addr = s.recvfrom(1024)
		print("Message From:"+str(addr))
		print("From connected user:"+data)
		data = data.upper()
		print("sending:"+data)
		s.sendto(data.encode('utf-8'))
	c.close()

if __name__ == '__main__':
	Main()
	
		
	
