from threading import Timer

flight = "BA009"
transitions = ['On Time - 16.05', 'Gate Open', 'Boarding at Gate 6', 'Flight Closing', 'Gate Closed']
delay = 5
tic_count = 0

def feeder():
    global tic_count
    t = Timer(delay, feeder)
    t.start()
    print("%d: Flight status [%s]: %s" % (tic_count, flight, transitions[tic_count]))
    if tic_count < len(transitions)-1: 
        tic_count = tic_count + 1
    else:
        tic_count = 0
    return

feeder()

