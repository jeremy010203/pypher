import socketserver, socket
import sys
import gopher

HOST = 'localhost'
SERVER_IP = 8000
PROXY_IP = 8004

def get_socket(ip, po):
    s = None

    for res in socket.getaddrinfo(ip, po, socket.AF_UNSPEC, socket.SOCK_STREAM):
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

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print("{} wrote: {}".format(self.client_address[0], self.data))
        rep = self.data.decode()

        with get_socket(HOST, SERVER_IP) as s:
            print('Sending ' + '.' + rep.split(' ')[1])
            s.sendall(b'.' + rep.split(' ')[1].encode())
            d = s.recv(1024)
            print('Received ' + d.decode())
            self.request.sendall(d)

server = socketserver.TCPServer((HOST, PROXY_IP), MyTCPHandler)
server.serve_forever()
