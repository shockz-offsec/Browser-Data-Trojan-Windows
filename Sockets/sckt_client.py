import socket
import tqdm
import os
import glob
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 8192


def send_file(filename, host, port):
    filesize = os.path.getsize(filename)
    sckt = socket.socket()
    sckt.connect((host, port))
    sckt.send(f"{filename}{SEPARATOR}{filesize}".encode())
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            sckt.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    sckt.close()