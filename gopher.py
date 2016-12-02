import sys
import os

def request(r, ip, port):
    rep = ''
    if str(r) == '\r\n':
        for l in os.scandir():
            if l.is_file():
                rep += "0" + l.name + '\t' + l.path + '\t' + ip + '\t' + str(port) + '\n'
            elif l.is_dir():
                rep += "1" + l.name + '\t' + l.path + '\t' + ip + '\t' + str(port) + '\n'
        return (rep + '.').encode()
    else:
        if os.path.exists(r):
            if os.path.isfile(r):
                with open(r, 'rb') as f:
                    return f.read() + b'\n.'
            else:
                for l in os.scandir(r):
                    if l.is_file():
                        rep += "0" + l.name + '\t' + l.path + '\t' + ip + '\t' + str(port) + '\n'
                    elif l.is_dir():
                        rep += "1" + l.name + '\t' + l.path + '\t' + ip + '\t' + str(port) + '\n'
                return (rep + '.').encode()
        else:
            return b'Error'
