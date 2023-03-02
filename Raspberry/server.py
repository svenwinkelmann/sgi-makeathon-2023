import socket
import tqdm
import os

SERVER_IP = "0.0.0.0"
SERVER_PORT = 35000

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()
s.bind((SERVER_IP, SERVER_PORT))
s.listen(5)
print("Server listening at IP: {} PORT: {}".format(SERVER_IP, SERVER_PORT))

while True:
    client_socket, address = s.accept()
    print("{} is connected".format(address))

    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    progress = tqdm.tqdm(range(filesize), "Receiving {}".format(filename), unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))

    print("File received")
    client_socket.close()
    
s.close()


