"""_summary_

    Using Asyncio library

"""

import asyncio
from typing import Generator

async def numbers(numbers)-> Generator[int, None, None]:
    for i in range(numbers):
        yield i
        await asyncio.sleep(0.5)

async def main()-> None:
    odd_numbers: list[int] = [i async for i in numbers(10) if i % 2 == 0]
    print(odd_numbers)
    
if __name__ == '__main__':
    event_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()