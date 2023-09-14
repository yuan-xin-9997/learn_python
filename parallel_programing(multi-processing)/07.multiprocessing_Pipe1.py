# -*- coding: utf-8 -*-

# File Name： 07.multiprocessing_Pipe1
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:
"""
进程间通信

多进程还有一种数据传递方式叫管道原理和 Queue相同。Pipe可以在进程之间创建一条管道，并返回元组（conn1,conn2）,其中conn1，conn2表示管道两端的连接对象，强调一点：必须在产生Process对象之前产生管道。
构造方法：Pipe([duplex])
dumplex:默认管道是全双工的，如果将duplex射成False，conn1只能用于接收，conn2只能用于发送。

"""

from multiprocessing import Process, Pipe

import time

# 子进程执行方法

def f(Subconn):

    time.sleep(1)

    Subconn.send("吃了吗")

    print("来自父亲的问候:", Subconn.recv())

    Subconn.close()

if __name__ == "__main__":

    parent_conn, child_conn = Pipe()  # 创建管道两端

    p = Process(target=f, args=(child_conn,))  # 创建子进程

    p.start()

    print("来自儿子的问候:", parent_conn.recv())

    parent_conn.send("嗯")
    p.join()