
events = ["evt1", "evt2", "evt3"]

def my_pop():
    if events:
        evt = events.pop(0)
        print(evt)

print(events)
my_pop()
my_pop()
my_pop()
my_pop()



