
import asyncio

async def func():
    print("快来搞我吧！")

result = func()
print(result)
loop = asyncio.get_event_loop()
loop.run_until_complete( result )

# 下面这句代码等价于上面两行
# asyncio.run( result ) # python3.7