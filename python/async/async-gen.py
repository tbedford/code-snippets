import asyncio

async def ag():
    for i in range(5):
        # Simulating some asynchronous operation
        await asyncio.sleep(1)
        yield i

async def main():
    async for item in ag():
        print(item)

asyncio.run(main())
