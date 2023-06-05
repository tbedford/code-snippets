import asyncio

# Simulate I/O-bound task that takes 1 second only
async def rt1():
    print("A")
    await asyncio.sleep(1) 
    print("B")

# This is a CPU-bound task that will block other
# co-routines. It shouldn't really be async, as it's
# CPU-bound rather than I/O bound.
async def rt2():
    print("CPU bound 1")
    for i in range (100000):
        for i in range (10000):
            pass
    print("CPU bound 2")


    
async def main():
    # calls to greet() do **not** block! 
    await asyncio.gather(
        rt1(),
        rt2(),
    )

asyncio.run(main())

