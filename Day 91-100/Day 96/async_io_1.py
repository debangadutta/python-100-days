import time
import asyncio

async def func1():
    await asyncio.sleep(2)
    print("func 1")
    return "Hello"

async def func2():
    await asyncio.sleep(2)
    print("func 2")

async def func3():
    await asyncio.sleep(5)
    print("func 3")

async def main():
    # task = asyncio.create_task(func1())
    # await func1()
    # await func2()
    # await func3()
    L = await asyncio.gather(func1(),
                            func2(),
                            func3())
    print(L)

asyncio.run(main())