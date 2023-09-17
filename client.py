if __name__ == "__main__":
	exit(0)

import socket
from threading import Thread


class Client():
	def __init__(self, addr="127.0.0.1", port=11719):
		self.addr = addr
		self.port = port

		self._create_socket()
		self._thread_type_message()

	def _thread_type_message(self):
		self.thread_type_message = Thread(target=self._type_message)
		self.thread_type_message.start()
	
	def _create_socket(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	
	def _type_message(self):
		while True:
			message = input("Type your message: ")
			self._send_message(message)
	
	def _send_message(self, message: str):
		self.sock.sendto(message.encode(),(self.addr,self.port))
