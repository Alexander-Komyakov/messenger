if __name__ == "__main__":
	exit(0)

import socket
from threading import Thread


class Server():
	def __init__(self, addr="192.168.3.17", port=11719):
		self.addr = addr
		self.port = port
		self._create_socket()
		self._bind_socket()
		self._thread_listen_socket()

	def _thread_listen_socket(self):
		self.thread_socket = Thread(target=self._listen_socket)
		self.thread_socket.start()
	
	def _create_socket(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	
	def _bind_socket(self):
		self.sock.bind((self.addr,self.port))
	
	def _listen_socket(self):
		while True:
			message = self.sock.recv(128).decode()
			print("\nMessage: "+message)
