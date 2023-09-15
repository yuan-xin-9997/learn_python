# -*- coding: utf-8 -*-

# File Name： 09.multiprocessing_Lock1
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:
"""
Lock（互斥锁）
Lock锁的作用是当多个进程需要访问共享资源的时候，避免访问的冲突。
加锁保证了多个进程修改同一块数据时，同一时间只能有一个修改，即串行的修改，牺牲了速度但保证了数据安全。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

本案例对比有添加锁，对数据同步的影响
"""
import time
import os
from multiprocessing import Process, Lock, Value, Array

###### 下面这种方式无法实现进程间数据共享，显然会导致数据有问题（这种全局变量无法被进程共享，所以就算加锁也无法实现同步，因为全局变量被各子进程拷贝到了各自内存空间中了）
class Balance:
    def __init__(self, value):
        self.value = value
# balance = Balance(1000)


###### 下面这种方式能够实现进程间数据共享，但是无法解决同步问题（因为没有加锁，用来实现同步）
balance = Value('d', 1000.0)
arr = Array('i', range(10))


###### 创建一个互斥锁，实现共享数据同步
lock = Lock()


def draw(balance, amount, lock):
    lock.acquire()
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
    lock.release()


if __name__ == "__main__":
    # lock = Lock()

    print(f"current process id = {os.getpid()}")
    pa = Process(name="process_A", target=draw, args=(balance, 800, lock))
    pb = Process(name="process_B", target=draw, args=(balance, 800, lock))

    pa.start()
    pb.start()

    pa.join()
    pb.join()