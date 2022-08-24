import asyncio
from util import delay
import time


async def main():
    start_time = time.time()
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await sleep_for_three
    await sleep_again
    await sleep_once_more
    print('Run time:', time.time() - start_time)


asyncio.run(main())
