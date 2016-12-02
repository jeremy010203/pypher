import socket, mysock
import sys

HOST = 'localhost'    # The remote host
PORT = sys.argv[1]

inp = input('>')
while inp != 'exit':
    with mysock.get_socket(HOST, PORT) as s:
        if inp == '':
            s.sendall(b'\r\n')
        else:
            s.sendall(inp.encode())
        data = s.recv(1024)
        print(data.decode())
        inp = input('>')
