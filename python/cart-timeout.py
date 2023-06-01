import threading
import time

# decrement cart timeout

callback_timer = 3
cart_timeout = 10
carts =  [{"id": 123, "count": 5}, {"id": 456, "count": 3}, {"id":789, "count": 8}]

def proc_carts(cts):
    print('Decrement cart timers')
    for c in cts:
        c["count"] = c["count"] - 1
        if c["count"] <= 0:
            print('send cart abandoned event for cart: ', c["id"])
            cts.pop(cts.index(c))
    print(cts)
    
def timer_callback(ct, c):
    print('Timer - callback')
    time.sleep(ct)
    proc_carts(c)
    timer_thread.run()

timer_thread = threading.Thread(target=timer_callback, args=(callback_timer, carts, ))
timer_thread.start()
