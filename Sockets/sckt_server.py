import socket
from tqdm import tqdm
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5678
BUFFER_SIZE = 8192
SEPARATOR = b"<SEPARATOR>"

sckt = socket.socket()
sckt.bind((SERVER_HOST, SERVER_PORT))

