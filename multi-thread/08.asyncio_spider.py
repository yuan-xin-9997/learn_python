"""
异步IO，协程，演示爬虫
协程：在单线程内实现并发核心原理：用一个超级循环（其实就是while true）
循环核心原理：配合路复用原理（IO时CPU可以干其他事情）
TODO：考虑多进程嵌套多线程嵌套多协程，能否更大的提高性能？
性能：对比单线程、多线程爬虫，可知，异步io（协程）>多线程>单线程，之所以比多线程高，是因为多线程有线程切换的耗时
"""
import asyncio
import aiohttp
import time
import blog_spider
from functools import wraps


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
    """定义一个协程，可以在超级循环中运行的函数"""
    print("craw url:",  url)
    async with aiohttp.ClientSession() as session:  # 由于request不支持await关键字，所以需要用aiohttp替代request
        async with session.get(url) as resp:
            result = await resp.text()
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












