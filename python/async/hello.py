import asyncio

async def greet(name):
    print("Hello,", name)
    await asyncio.sleep(3)
    print("Goodbye,", name)

async def main():
    # calls to greet() do **not** block! 
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    )

asyncio.run(main())

