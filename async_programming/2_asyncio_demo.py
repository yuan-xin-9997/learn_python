"""
使用asyncio实现协程，使用Python标准库（Python>3.4）,即一个线程在多个函数之间切换
由于版本原因，此demo使用async和await关键字

协程的意义：在一个线程中如果遇到IO等待时间，线程不会傻等，利用空闲的时间再去执行其他代码。
"""

import asyncio

"""
DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
"""
# @asyncio.coroutine
async def func1():
    print(1)

    # "yield from" not allowed in an async function
    # yield from asyncio.sleep(2) # 遇到 IO 耗时操作，自动化切换到 tasks 中的其他任务 print (2)
    await asyncio.sleep(2)  # 遇到IO（sleep、网络请求、数据库连接等）阻塞，会自动切换线程
    print(2)


# @asyncio.coroutine 
async def func2():
    print(3)

    # yield from asyncio.sleep(2) # 遇到 IO 耗时操作，自动化切换到 tasks 中的其他任务 print (4)
    await asyncio.sleep(2)  # 遇到IO阻塞，会自动切换
    print(4)

tasks = [
    asyncio.ensure_future(func1()), 
    asyncio.ensure_future(func2())
]



loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))