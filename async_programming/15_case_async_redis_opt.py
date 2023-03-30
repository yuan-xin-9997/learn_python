import asyncio
import aioredis


async def execute(address, password):
    print("开始执行", address)

    # 网络IO操作：先去连接 47.93.4.197:6379，遇到IO则自动切换任务，去连接47.93.4.198:6379
    redis = await aioredis.create_redis_pool(address, password=password)

    # 网络IO操作：遇到IO会自动切换任务
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    # 网络IO操作：遇到IO会自动切换任务
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    redis.close()
    # 网络IO操作：遇到IO会自动切换任务
    await redis.wait_closed()

    print("结束", address)


task_list = [
    execute('redis://47.93.4.197:6379', "root!2345"),
    execute('redis://47.93.4.198:6379', "root!2345")
]

asyncio.run(asyncio.wait(task_list))