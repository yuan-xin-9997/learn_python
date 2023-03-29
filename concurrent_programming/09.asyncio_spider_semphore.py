"""
异步IO，协程，使用信号量机制控制并发度
"""
import asyncio
import aiohttp
import time
import blog_spider
from functools import wraps


semaphore = asyncio.Semaphore(10)


def time_this(func):
    """统计函数func的运行时间"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('函数{}.{}运行时间 : {} 秒'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


async def async_craw(url):
    """定义一个协程，可以在超级循环中运行的函数
    由于有了信号量，线程最多同时只有10个在执行
    """
    async with semaphore:
        print("craw url:",  url)
        async with aiohttp.ClientSession() as session:  # 由于request不支持await关键字，所以需要用aiohttp替代request
            async with session.get(url) as resp:
                result = await resp.text()
                await asyncio.sleep(5)
                print(f"craw url: {url}, {len(result)}")

# 建立超级循环
loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]


@time_this
def main():
    loop.run_until_complete(asyncio.wait(tasks))


main()












