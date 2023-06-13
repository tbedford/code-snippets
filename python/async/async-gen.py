import asyncio

# test

async def ag(n):
    for i in range(n):
        # Simulating some asynchronous operation
        await asyncio.sleep(1)
        yield i

async def main():
    async for item in ag(5):
        print(item)

# main loop        
asyncio.run(main())

