import socket

HOST = "127.0.0.1"
PORT = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

try:
    while True:
        message = input("Input: ")
        sock.sendall(message.encode("utf-8"))

        # RECEIVE RESPONSE
        data = sock.recv(4096)
        if not data:
            print("Server closed connection")
            break

        print("Received:", data.decode("utf-8"))

finally:
    sock.close()
