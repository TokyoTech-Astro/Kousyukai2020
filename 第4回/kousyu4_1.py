from threading import Thread
import time

boolean=True

class counter(Thread):
    def __init__(self):
        super(counter,self).__init__()
    
    def run(self):
        t = 0
        while boolean:
            print(t)
            t += 1
            time.sleep(0.3)

thread1 = counter()
thread1.start()

while 1:
    if input() == "end":
        boolean = False
        break

#thread1.join()
print("end")
