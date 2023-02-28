import socket
import tqdm
import os
import argparse
import random
import datetime

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

#send file to Server
def send_file(filename, host, port):
    filesize = os.path.getsize(filename)
    s = socket.socket()
    s.connect((host, port))
    print("Connected to server")

    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), "Sending {}".format(filename), unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
        
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

    s.close()
    print("Transfer complete")

#Write data to file
def write_file():
    f = open(filename, "w")
    f.write("Temp: {}°C\n".format(random.randint(0, 40)))
    f.write("Humidity: {}%\n".format(random.randint(0, 100)))
    f.write("Timestamp: {}".format(datetime.datetime.now()))
    f.close()

if __name__ =="__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Sender")
    parser.add_argument("file", help="File name to send", default = "test2.txt")
    parser.add_argument("host", help="Host IP of receiver")
    parser.add_argument("-p", "--port", help="Ports to use, default 35000", default = 35000)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    #write_file()
    send_file(filename, host, port)
    
