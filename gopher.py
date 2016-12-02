import sys
import os

def file_type(f):
    if f.is_file():
        return "0"
    elif f.is_dir():
        return "1"
    else:
        return "3"

def scandir(dr, ip, port):
    r = ''
    for l in os.scandir(dr):
        r += "{}{}\t{}\t{}\t{}\n".format(file_type(l), l.name, l.path, ip, str(port))
    return r + '.'

def read_file(r):
    with open(r, 'rb') as f:
        return f.read() + b'\n.'

def request(r, ip, port):
    if str(r) == '\r\n':
        return scandir('.', ip, port).encode()
    else:
        if os.path.exists(r):
            return read_file(r) if os.path.isfile(r) else scandir(r, ip, port).encode()
        else:
            return b'Error'

def html_to_gopher(r):
    return b'.' + r.split(' ')[1].encode()
