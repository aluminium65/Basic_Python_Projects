import socket
import threading


IP = '0.0.0.0'
PORT = 9997


print("""
    _             _______      _____
   |#|          _|# # # #|    |# # #|_
 __|#|__       |#|            |#     #|      @@@@ @@@@ @@@  @   @ @@@@ @@@
|# # # #|      |#|            |#     #|      @    @    @  @ @   @ @    @  @
   |#|    _    |#|            |# # #|        @@@@ @@@@ @@@  @   @ @@@@ @@@
   |#|___|#|   |#|_______     |#|               @ @    @ @   @ @  @    @ @
   |# # # #|     |# # # #|    |#|            @@@@ @@@@ @  @   @   @@@@ @  @

      
------------------------------By aluminium----------------------------------      
""")
git = "\n[GITHUB]: https://github.com/aluminium65/Python-Projects"
print(git)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")
    print("[*] Press Ctrl + C to exit.")

    try:
        while True:
            client, address = server.accept()
            print(f"[*] Accepted connection from {address[0]}:{address[1]}")
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()

    except KeyboardInterrupt:
        print("\n[*] Exiting!")
        server.close() 


def handle_client(client_socket):
    with client_socket as sock:
        while sock:
            sock.send(b" >> ")
            request = sock.recv(1024)
            if request:
                message = request.decode("utf-8")
                print(f"[*] Recieved: {message.replace("\n", "")}")


if __name__== "__main__": 
    main()
