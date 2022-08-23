# import asyncio
# import random
#
# # ANSI colors
# c = (
#     "\033[0m",  # End of color
#     "\033[36m",  # Cyan
#     "\033[91m",  # Red
#     "\033[35m",  # Magenta
# )
#
#
# async def makerandom(idx: int, threshold: int = 6) -> int:
#     print(c[idx + 1] + f"Initiated makerandom({idx}).")
#     i = random.randint(0, 10)
#     while i <= threshold:
#         print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
#         await asyncio.sleep(idx + 1)
#         i = random.randint(0, 10)
#     print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
#     return i
#
#
# async def main():
#     print(*(makerandom(i, 10 - i - 1) for i in range(3)))
#     print(type(*(makerandom(i, 10 - i - 1) for i in range(3))))
#     res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
#     return res
#
#
# if __name__ == "__main__":
#     random.seed(444)
#     r1, r2, r3 = asyncio.run(main())
#     print()
#     print(f"r1: {r1}, r2: {r2}, r3: {r3}")


# import asyncio
# import random
# import time
#
#
# async def part1(n: int) -> str:
#     i = random.randint(0, 10)
#     print(f"part1({n}) sleeping for {i} seconds.")
#     await asyncio.sleep(i)
#     result = f"result{n}-1"
#     print(f"Returning part1({n}) == {result}.")
#     return result
#
#
# async def part2(n: int, arg: str) -> str:
#     i = random.randint(0, 10)
#     print(f"part2{n, arg} sleeping for {i} seconds.")
#     await asyncio.sleep(i)
#     result = f"result{n}-2 derived from {arg}"
#     print(f"Returning part2{n, arg} == {result}.")
#     return result
#
#
# async def chain(n: int) -> None:
#     start = time.perf_counter()
#     p1 = await part1(n)
#     p2 = await part2(n, p1)
#     end = time.perf_counter() - start
#     print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")
#
#
# async def main(*args):
#     await asyncio.gather(*(chain(n) for n in args))
#
#
# if __name__ == "__main__":
#     import sys
#
#     random.seed(444)
#     args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
#     start = time.perf_counter()
#     asyncio.run(main(*args))
#     end = time.perf_counter() - start
#     print(f"Program finished in {end:0.2f} seconds.")

import asyncio
import time


async def main():
    start = time.time()
    print("Hello")
    # await foo('text')
    task = asyncio.create_task(foo('text'))
    # await task
    # await asyncio.sleep(5)

    sleep_for_three = asyncio.create_task(asyncio.sleep(3))
    sleep_again = asyncio.create_task(asyncio.sleep(3))
    # sleep_once_more = asyncio.create_task(asyncio.sleep(3))

    await hello_every_second()
    await sleep_for_three
    await sleep_again
    # await sleep_once_more
    # print(task)
    # await task
    print("END")
    print('runtime', time.time() - start)

async def foo(text):
    print(text)
    await asyncio.sleep(100)

async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting!")

asyncio.run(main())
