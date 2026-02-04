import socket
import time

HOST = "127.0.0.1"  # Replace with server IP if not local
PORT = 8081          # Same port your server is listening on

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

try:
    while True:
        message = "signal sent"
        # Convert string to bytes
        data = message.encode("utf-8")

        # Send binary data
        sock.sendall(data)
        print(f"Sent: {message}")

        # Wait 5 seconds
        time.sleep(5)
finally:
    sock.close()
    print("Connection closed")
