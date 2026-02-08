"""Simple TCP Server that demonstrates raising and handling
HTTP-style errors (401, 402, 403, 404) using exceptions.
Clients send a short code (e.g., "401") or any message. Server
raises a corresponding exception and sends back an error message.
"""

import socket


class HTTPError(Exception):
	def __init__(self, code: int, message: str):
		super().__init__(f"{code} {message}")
		self.code = code
		self.message = message


class Unauthorized(HTTPError):
	def __init__(self):
		super().__init__(401, "Unauthorized")


class PaymentRequired(HTTPError):
	def __init__(self):
		super().__init__(402, "Payment Required")


class Forbidden(HTTPError):
	def __init__(self):
		super().__init__(403, "Forbidden")


class NotFound(HTTPError):
	def __init__(self):
		super().__init__(404, "Not Found")


def process_request(data: str) -> bytes:
	"""Process incoming request string and either return a normal
	response or raise an HTTPError for certain codes.
	"""
	data = data.strip()
	# Raise exceptions for specific codes
	if data == "401":
		raise Unauthorized()
	if data == "402":
		raise PaymentRequired()
	if data == "403":
		raise Forbidden()
	if data == "404":
		raise NotFound()

	# Normal processing
	return f"200 OK: Received '{data}'".encode()


def main():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server_socket.bind(('localhost', 8008))
		server_socket.listen(1)
		print("Server is listening on port 8008...")

		# Accept multiple connections in a loop until interrupted
		while True:
			try:
				conn, addr = server_socket.accept()
			except KeyboardInterrupt:
				print("Server interrupted while waiting for connection.")
				break
			except Exception as e:
				print(f"Accept error: {e}")
				break

			print(f"Connection from {addr} has been established!")
			try:
				raw = conn.recv(1024)
				if not raw:
					print("No data received.")
					conn.close()
					continue
				data = raw.decode()
				print(f"Received data: {data}")
				try:
					response = process_request(data)
				except HTTPError as he:
					# Catch HTTP-style exceptions and send error message
					err_msg = f"{he.code} {he.message}"
					print(f"Handled error: {err_msg}")
					conn.send(err_msg.encode())
				else:
					conn.send(response)
			except Exception as conn_e:
				print(f"Error during connection handling: {conn_e}")
			finally:
				try:
					conn.close()
				except Exception:
					pass

	except KeyboardInterrupt:
		print("Server interrupted by user.")
	except Exception as e:
		print(f"Server error: {e}")
	finally:
		try:
			server_socket.close()
		except Exception:
			pass


if __name__ == '__main__':
	main()