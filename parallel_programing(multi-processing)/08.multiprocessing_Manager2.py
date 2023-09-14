# -*- coding: utf-8 -*-

# File Name： 08.multiprocessing_Manager2.py
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:
import os
import time
from multiprocessing import Process, Manager


"""
Manger 这种方式能够实现进程间数据共享，但是无法解决同步问题
"""


###### 下面这种方式无法实现进程间数据共享，显然会导致数据有问题
# class Balance:
#     def __init__(self, value):
#         self.value = value
# # balance = Balance(1000)


###### 下面这种方式能够实现进程间数据共享，但是无法解决同步问题
# balance = Value('d', 1000.0)
# arr = Array('i', range(10))

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
    server = Manager()
    balance = server.Value('d', 1000.0)

    print(f"current process id = {os.getpid()}")
    pa = Process(name="process_A", target=draw, args=(balance, 800))
    pb = Process(name="process_B", target=draw, args=(balance, 800))

    pa.start()
    pb.start()

    pa.join()
    pb.join()