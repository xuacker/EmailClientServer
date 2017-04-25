from socket import *
import threading
import ssl


class server_thread(threading.Thread):
    def __init__(self, acceptedConnection):
        threading.Thread.__init__(self)
        self.socket, self.addr = acceptedConnection
    def run(self):
		print("Allocating a new thread for the connection that was just recieved")
		print '-------------------------------------------------------'
		self.socket.send('hi and welcome')
		try:
			while 1:
				sentence = self.socket.recv(1024)
				if not sentence:
					break
				print sentence
		except KeyboardInterrupt:			
			self.socket.shutdown(SHUT_RDWR)
			self.socket.close()	
	


class socketThreadHandler():
    def __init__(self):
		SMTPport = 465
		IMAPport = 1
		self.socket = socket(AF_INET,SOCK_STREAM)
		SMTPwelcomeSocket = ssl.wrap_socket(self.socket,server_side=True,certfile='cacert.pem',keyfile='private.pem')
		SMTPwelcomeSocket.bind(('',SMTPport))
		SMTPwelcomeSocket.listen(1)
		print 'Server is now taking requests'
		print "=============================================="
		while 1:
			server_thread(SMTPwelcomeSocket.accept()).start()


socketThreadHandler()
		