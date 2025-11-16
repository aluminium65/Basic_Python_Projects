import socket
import threading

IP = "localhost"
PORT = 1988

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP, PORT))
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.listen(5)
	print("[GITHUB] https://github.com/aluminium65")
	print(f"[+] Listening on {IP}:{PORT}")
	print("[+] Enter Ctrl + C to exit.")
	try:
		while True:
			client, address = server.accept()
			print(f"[+] Accepted connection from {address[0]}")
			handler = threading.Thread(target=handle_client, args=(client, address[0]))
			handler.start()

	except KeyboardInterrupt:
		print("\b\b[+] Exiting...")
		server.close()
		exit()

def handle_client(client_socket, addr):
	with client_socket as sock:
		response = sock.recv(1024)
		if response:
			print(f"[{addr}]" + response.decode())
		sock.send(b"[+] TCP_Server says Hello!")

if __name__ == "__main__":
	main()