from threading import Thread
import time

boolean=True

class counter(Thread):
    def __init__(self):
        super(counter,self).__init__()
    
    def run(self):
        # TODO

thread1 = counter()
thread1.start()

while 1:
    if input() == "e":
        boolean = False
        break

print("end")
