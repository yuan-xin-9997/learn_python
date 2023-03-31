import asyncio


async def func(n):
    print(n)
    await asyncio.sleep(2)
    print(n+1)
    return "返回值"


"""
直接下面这么写会报错：RuntimeError: no running event loop
sys:1: RuntimeWarning: coroutine 'func' was never awaited

因为asyncio.run之前还没有创建事件循环

task_list = [
        asyncio.create_task(func(1), name='n1'),
        asyncio.create_task(func(3), name='n2')
    ]
done, pending = asyncio.run( task_list )
"""

task_list = [
        func(1),
        func(3)
    ]

done, pending = asyncio.run(
    asyncio.wait(task_list)  # 会调用ensure_future，将task_list的函数包装为协程对象
)
print(done)
print(pending)