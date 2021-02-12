import asyncio 

async def make_americano():
    print("Americano Start")
    await asyncio.sleep(3)
    print("Americano End")
    return "Americano"

async def make_latte():
    print("Latte Start")
    await asyncio.sleep(5)
    print("Latte End")
    return "Latte"

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    result = await asyncio.gather(
        coro1, 
        coro2
    )
    print(result)

print("Main Start")
asyncio.run(main())
print("Main End")