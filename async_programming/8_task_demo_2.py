import asyncio


async def func(n):
    print(n)
    await asyncio.sleep(2)
    print(n+1)
    return "返回值"


# def main():  # SyntaxError: 'await' outside async function
async def main():
    print("main开始")

    task_list = [
        asyncio.create_task(func(1), name='n1'),  # create_task 返回一个Task对象
        asyncio.create_task(func(3), name='n2')   # create_task 返回一个Task对象
    ]

    print("main结束")

    # 由于有了Task，才实现了提高性能和速度
    done, pending = await asyncio.wait(task_list, timeout=None)   # asyncio.wait等待所有task执行完毕，返回执行结果
    print(done)
    print(pending)


asyncio.run(main())  # asyncio.run( ... )相当于创建了一个事件循环，等价于 loop = asyncio.get_event_loop();  loop.run_until_complete( result )
# main()  # RuntimeWarning: coroutine 'main' was never awaited
