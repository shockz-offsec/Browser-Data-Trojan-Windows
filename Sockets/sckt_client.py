import socket
from tqdm import tqdm
import os
import glob
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 8192


def send_file(filename, host, port):
    filesize = os.path.getsize(filename)
    sckt = socket.socket()
    sckt.connect((host, port))
    sckt.send(f"{filename}{SEPARATOR}{filesize}".encode())
    with open(filename, "rb") as f:
        for _ in tqdm(range(100)):
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            sckt.sendall(bytes_read)

    sckt.close()