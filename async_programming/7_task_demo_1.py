import asyncio
import time


async def func(n):
    print(n)
    await asyncio.sleep(2)
    # asyncio.sleep(2)
    # time.sleep(2)
    print(n+1)
    return "返回值"


async def main():
    print("main开始")

    # 创建Task对象，将当前执行func函数任务添加到事件循环。
    task1 = asyncio.create_task(func(1))

    # 创建Task对象，将当前执行func函数任务添加到事件循环。
    task2 = asyncio.create_task(func(3))

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动化切换执行其他任务。
    # 此处的await是等待相对应的协程全都执行完毕并获取结果
    ret1 = await task1
    # ret1 = task1
    ret2 = await task2
    # ret2 = task2
    print(ret1, ret2)


asyncio.run(main())