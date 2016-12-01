import sys
import os

def request(r, ip, port):
    print("Gopher: Received: " + str(r))
    if str(r) == '\r\n' or str(r) == '\n':
        rep = ''
        for l in os.scandir():
            if l.is_file():
                rep += "0" + l.name + '\t' + l.path + '\t' + ip + '\t' + port + '\n'
            if l.is_dir():
                rep += "1" + l.name + '\t' + l.path + '\t' + ip + '\t' + port + '\n'
        return rep + '.'
    else:
        return 'Error: bad syntax: ' + str(r)
