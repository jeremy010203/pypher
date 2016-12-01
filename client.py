import socket
import sys

HOST = 'localhost'    # The remote host
PORT = sys.argv[1]

def get_socket():
    global HOST
    global PORT
    s = None

    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except OSError as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print('could not open socket')
        sys.exit(1)
    return s

inp = input('>')
while inp != 'exit':
    with get_socket() as s:
        if inp == '':
            s.sendall(b'\r\n')
        else:
            s.sendall(inp.encode())
        data = s.recv(1024)
        print(data.decode())
        inp = input('>')
