from threading import Thread
import time

def callback(a, b):
    time.sleep(1)
    print(a)
    print(b)
    t.run()
    
t = Thread(target=callback, args=("hi", "hello"))

t.start()
