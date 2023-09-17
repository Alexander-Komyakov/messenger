from server import Server
from client import Client
import argparse
import sys

def main()->int:
	parser = argparse.ArgumentParser()
	parser.add_argument("-cp", "--cport", default="11719")
	parser.add_argument("-ca", "--caddress", default="127.0.0.1")
	parser.add_argument("-sp", "--sport", default="11719")
	parser.add_argument("-sa", "--saddress", default="127.0.0.1")
	all_args = parser.parse_args(sys.argv[1:])

	client_port = int(all_args.cport)
	client_address = all_args.caddress
	server_port = int(all_args.sport)
	server_address = all_args.saddress


	server = Server(server_address, server_port)
	client = Client(client_address, client_port)
	return 0

if __name__ == "__main__":
	main()

