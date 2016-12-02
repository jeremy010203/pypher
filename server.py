import socketserver
import sys
import gopher

HOST = 'localhost'
PORT = int(sys.argv[1])

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print("{} wrote: {}".format(self.client_address[0], self.data))
        self.request.sendall(gopher.request(self.data.decode(), HOST, PORT))

server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()
