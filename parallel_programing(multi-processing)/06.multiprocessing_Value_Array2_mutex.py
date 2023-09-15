# -*- coding: utf-8 -*-

# File Name： 06.multiprocessing_Value_Array2_mutex
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:
"""
进程之间通信、共享数据
借助Value、Array实现同步，对比没有实现Value，直接使用全局变量（无法实现同步）
"""
import os
import time
from multiprocessing import Process, Value, Array


###### 下面这种方式无法实现进程间数据共享（每个进程会拷贝一份放置到自己的内存全局区域），显然会导致数据有问题，余额都是200元
class Balance:
    def __init__(self, value):
        self.value = value
# balance = Balance(1000)


###### 下面这种方式能够实现进程间数据共享，但是无法解决同步问题，余额都是-600元，显然是不符合的
balance = Value('d', 1000.0)
arr = Array('i', range(10))


def draw(balance, amount):
    if balance.value >= amount:
        print(
            os.getpid(), f"parent process id = {os.getppid()}，取钱之前，余额{balance.value}"
        )
        time.sleep(0.1)  # 由于sleep会发生线程阻塞，模拟IO场景，导致线程切换，因此执行结果一定是错误的
        print(
            os.getpid(), f"parent process id = {os.getppid()}，取钱成功"
        )
        balance.value -= amount
        print(
            os.getpid(), f"parent process id = {os.getppid()}，取钱之后，余额{balance.value}"
        )
    else:
       print(
            os.getpid(), f"parent process id = {os.getppid()}，取钱失败，余额不足"
        )


if __name__ == "__main__":
    # balance = Value('d', 1000.0)

    print(f"current process id = {os.getpid()}")
    pa = Process(name="process_A", target=draw, args=(balance, 800))
    pb = Process(name="process_B", target=draw, args=(balance, 800))

    pa.start()
    pb.start()

    pa.join()
    pb.join()
