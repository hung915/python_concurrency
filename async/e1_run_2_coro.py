import asyncio
from util import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world() -> str:
    await delay(1)
    return 'HelloWorld!'


async def main() -> None:
    message = await hello_world()
    one_plus_one = await add_one(1)
    print(message)
    print(one_plus_one)


asyncio.run(main())
