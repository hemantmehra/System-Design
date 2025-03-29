import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen()

while True:
    conn, addr = s.accept()
    print(f"Connection: {addr}")
    data = conn.recv(1024)
    conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nHello world!\r\n")
    conn.close()
