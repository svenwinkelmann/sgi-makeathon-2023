import threading
import time

def task():
    for i in range(0,10):
        print(i)
        time.sleep(1)

thread = threading.Thread(target=task)
thread.setDaemon(True)

thread.start()

print("waiting for Thread")

while(True):
    time.sleep(1)
