import asyncio

import uvicorn
import aioredis
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()

# 创建一个redis连接池
REDIS_POOL = aioredis.ConnectionsPool('redis://47.193.14.198:6379', password="root123", minsize=1, maxsize=10)


@app.get("/")
def index():
    """ 普通操作接口 """
    return {"message": "Hello World"}


@app.get("/red")
async def red():
    """ 异步操作接口 """
    
    print("请求来了")

    await asyncio.sleep(3)
    # 连接池获取一个连接
    conn = await REDIS_POOL.acquire()
    redis = Redis(conn)

    # 设置值
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    # 读取值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    # 连接归还连接池
    REDIS_POOL.release(conn)

    return result


if __name__ == '__main__':
    uvicorn.run("17_case_fastapi_async_opt:app", host="127.0.0.1", port=5000, log_level="info")