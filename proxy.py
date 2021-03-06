import socketserver, socket, mysock
import sys
import gopher

HOST = 'localhost'
SERVER_IP = 8000
PROXY_IP = 8004

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print("{} wrote: {}".format(self.client_address[0], self.data))
        rep = gopher.html_to_gopher(self.data.decode())

        with mysock.get_socket(HOST, SERVER_IP) as s:
            s.sendall(rep)
            d = s.recv(1024)
            self.request.sendall(gopher.gopher_to_html(d.decode()).encode())

server = socketserver.TCPServer((HOST, PROXY_IP), MyTCPHandler)
server.serve_forever()
