"""
异步IO，协程，使用信号量机制控制并发度

异步编程介绍：
Python中的async和await关键字是用于异步编程的语法糖。在异步编程中，任务不会阻塞主线程，而是在后台运行，从而提高程序的效率和响应速度
async关键字用于定义一个异步函数，异步函数可以在后台运行，而不会阻塞主线程。例如
async def foo():
    # do some async task

await关键字用于等待一个异步任务完成。在异步函数中，可以使用await关键字等待另一个异步函数的完成。例如：
async def bar():
    result = await foo()
    # do something with the result
在上面的代码中，bar函数中的await关键字等待foo函数的完成，然后将结果赋给result变量。
需要注意的是，异步函数必须使用async关键字定义，并且必须在异步函数中使用await关键字来等待其他异步函数的完成。
此外，异步函数可以使用asyncio模块来管理异步任务的调度和协调。

使用async和await关键字可以使异步编程变得更加简单和直观。在异步编程中，可以使用异步协程来执行耗时的任务，而不会阻塞主线程。异步协程可以使用async
和await关键字来定义和执行。
例如，下面的代码使用异步协程来执行一个耗时的任务：
import asyncio
async def task():
    print('start task')
    await asyncio.sleep(1)
    print('end task')
async def main():
    print('start main')
    await task()
    print('end main')
asyncio.run(main())
在上面的代码中，task函数使用await关键字等待1秒钟，然后打印“end task”。main函数使用await关键字等待task函数完成，然后打印“end main”。最后，
使用asyncio.run()函数来启动异步协程。

需要注意的是，异步协程必须在异步上下文中执行。在Python中，可以使用asyncio模块来管理异步上下文，并协调异步任务的执行。例如，使用asyncio.run()
函数来启动异步协程，使用asyncio.sleep()函数来暂停异步协程的执行，使用asyncio.wait()函数来等待多个异步任务的完成。

总之，async和await关键字是Python中用于异步编程的语法糖。它们使异步编程变得更加简单和直观，可以提高程序的效率和响应速度。

Q1：多线程和多进程是同步还是异步的?
A1：多线程和多进程都可以是同步或异步的，这取决于具体的实现方式和代码逻辑。
同步操作是指程序执行的顺序是按照代码的顺序来执行的，每个操作都必须等待前一个操作完成后才能执行下一个操作。
在同步模式下，每个线程或进程都是按照顺序依次执行的，直到完成所有的操作。
异步操作是指程序不会按照代码的顺序执行，而是在等待某些操作完成的同时，可以继续执行其他操作。在异步模式下，
每个线程或进程可以同时执行多个操作，而不需要等待前一个操作的完成。
多线程和多进程都可以使用同步或异步的方式来实现。在多线程中，可以使用锁来实现同步操作，也可以使用异步编程技术来实现异步操作。
在多进程中，可以使用进程间通信机制来实现同步操作，也可以使用异步编程技术来实现异步操作。
总的来说，多线程和多进程都可以实现同步或异步操作，具体取决于代码实现方式和逻辑。

Q2：异步编程使用信号量，与线程池通过控制池中线程数量大小，来控制并发度有何不一样
A2：异步编程中使用信号量和线程池控制并发度的方式不同，但目的相同，都是为了控制并发量，提高程序的效率和响应速度。
在异步编程中，信号量是一种用于控制并发度的机制，它可以限制同时执行的协程数量。例如，使用asyncio.Semaphore来控制同时最多有n个协程在执行。当
需要执行新的协程时，如果当前正在执行的协程数量已达到n，则新的协程必须等待其他协程执行完成后才能执行。
相比之下，线程池控制并发度的方式是通过控制线程池中线程的数量来限制并发量。线程池中的线程数量是固定的，当需要执行新的任务时，如果线程池中的线
程已全部占用，则新的任务必须等待线程池中的某个线程空闲后才能执行。
虽然两种方式的实现方式不同，但它们的目的都是为了控制并发量，避免程序因过多的并发而导致性能下降或崩溃。

相对于线程池，异步编程使用信号量的优势在于：
1.轻量级：协程比线程更加轻量级，可以在同样的硬件环境下支持更多的并发量；
2.更加灵活：协程可以在等待I/O操作的同时执行其他的任务，从而提高程序的效率和响应速度；
3.更加高效：协程的切换开销比线程小，可以更加高效地处理大量的并发任务。

需要注意的是，使用信号量和线程池控制并发度都需要合理地设置参数，避免过多或过少的并发导致性能下降或崩溃。同时，需要考虑任务的执行顺序和协调异步任务
的完成，避免死锁和竞态条件等问题，以确保程序的正确性和稳定性。
总之，异步编程使用信号量和线程池控制并发度的方式不同，但目的相同，都是为了控制并发量，提高程序的效率和响应速度。使用信号量控制并发度的优势在于轻量
级、更加灵活和更加高效，但需要合理设置参数，避免过多或过少的并发导致性能下降或崩溃。

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











