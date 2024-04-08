import socket
import time

Host = "0.0.0.0"
Port = 80

try:
	while True:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((Host, Port))
			s.listen()
			conn, addr = s.accept()
			with conn:
				print(f"Connected by {addr}")
				while True:
					data = conn.recv(2048)
					if not data:
						break
					#conn.sendall(data)
					time.sleep(1)
		time.sleep(1)
except KeyboardInterrupt:
	pass
