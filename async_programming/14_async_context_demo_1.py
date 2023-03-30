import asyncio


class AsyncContextManager:
    def __init__(self):
        self.conn = "conn"
        
    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步链接数据库
        # 上下文开始时候要做的操作
        print("start")
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # 异步关闭数据库链接
        # 上下文结束的时候要做的操作
        await asyncio.sleep(1)
        print("end")

async def func():
    # 异步上下文管理器也必须放在协程函数中
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)

asyncio.run( func() )