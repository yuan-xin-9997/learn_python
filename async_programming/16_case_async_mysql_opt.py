import asyncio
import aiomysql


async def execute(host, password):
    print("开始", host)
    # 网络IO操作：先去连接 47.93.40.197，遇到IO则自动切换任务，去连接47.93.40.198:6379
    conn = await aiomysql.connect(host=host, port=3306, user='root', password=password, db='mysql')

    # 网络IO操作：遇到IO会自动切换任务
    cur = await conn.cursor()

    # 网络IO操作：遇到IO会自动切换任务
    await cur.execute("SELECT Host,User FROM user")

    # 网络IO操作：遇到IO会自动切换任务
    result = await cur.fetchall()
    print(result)

    # 网络IO操作：遇到IO会自动切换任务
    await cur.close()
    conn.close()
    print("结束", host)


task_list = [
    execute('47.93.41.197', "root!2345"),
    execute('47.93.40.197', "root!2345")
]

asyncio.run(asyncio.wait(task_list))