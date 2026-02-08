"""Simple TCP Client that can request HTTP-style error codes.
Usage:
  python client.py 401    # send '401' to server
  python client.py        # prompts for input
"""

import socket
import sys


def main(msg: str):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client_socket.connect(('localhost', 8008))
		client_socket.send(msg.encode())
		data = client_socket.recv(1024).decode()
		print(f"Received data: {data}")
	except ConnectionRefusedError:
		print("Connection refused: is the server running on localhost:8008?")
	except Exception as e:
		print(f"Client error: {e}")
	finally:
		try:
			client_socket.close()
		except Exception:
			pass


if __name__ == '__main__':
	if len(sys.argv) > 1:
		message = sys.argv[1]
	else:
		message = input('Enter message or code (e.g. 401): ').strip()
	main(message)
