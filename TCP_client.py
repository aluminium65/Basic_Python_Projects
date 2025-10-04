import socket
import sys

print("""
    _             _______      _____
   |#|          _|# # # #|    |# # #|_
 __|#|__       |#|            |#     #|      @@@@@ @    @@@@@@@ @@@@ @     @ @@@@@@@
|# # # #|      |#|            |#     #|      @     @       @    @    @ @   @    @
   |#|    _    |#|            |# # #|        @     @       @    @@@@ @  @  @    @
   |#|___|#|   |#|_______     |#|            @     @       @    @    @   @ @    @
   |# # # #|     |# # # #|    |#|            @@@@@ @@@@ @@@@@@@ @@@@ @     @    @

      
------------------------------By aluminium----------------------------------      
""")
git = "\n[GITHUB]: https://github.com/aluminium65/Python-Projects"
print(git)

print("Enter The IP address of the target:")
target_host = input("  >> ")

print("Enter the port number:")
target_port = input("  >> ")
target_port = int(target_port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((target_host, target_port))

except ConnectionRefusedError:
    print(f"[Error] Connection refused by {target_host}")
    sys.exit()
    
except TimeoutError:
    print("[Error] Connection request timed out")
    sys.exit()

except:
    print("[Error] Unable to connect. Check the IP and port then try again.")
    sys.exit()

print("\nConnection Successful")
print("\nPress Ctrl + C to exit")
while True:
    
    try:
        print("\nType the message and press Enter to send.")
        msg = input(">> ")
        msg = msg.encode('utf-8')
        client.send(msg)
        print("Waiting for reply...\n")
        response = client.recv(4096)
        print(response.decode())
    
    except KeyboardInterrupt:
        print("Exiting....")
        break
        client.close()
