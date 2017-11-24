import socket

def Main():
	host = '127.0.0.1'
	port = 5051
	
	server = ('127.0.0.1',5050)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host,port))

	message = input("->")
	while message != 'q':
		s.send(message.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		addr = s.recv(1024)
		print("Received from server"+data)
		message=input("->")
	s.close()

if __name__ =="__main__":
	Main()
