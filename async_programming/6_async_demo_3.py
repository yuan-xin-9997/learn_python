import asyncio


async def others():
    print("start")
    await asyncio.sleep(2)
    print('end')
    return '返回值'


async def func():
    print("执行协程函数内部代码")

    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response1 = await others()
    # response1 = others()  # RuntimeWarning: coroutine 'others' was never awaited
    print("IO请求结束，结果为：", response1)

    response2 = await others()
    # response2 = others() # RuntimeWarning: coroutine 'others' was never awaited
    print("IO请求结束，结果为：", response2)


asyncio.run(func())