# -*- coding: utf-8 -*-

# File Name： 04.multiprocessing_pool3
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:

# 异步进程池（非阻塞）
import os
import time
from multiprocessing import Pool
from datetime import datetime

def main(i):
    print(f"{datetime.now()} current pid = {os.getpid()}, the value = {i}")
    time.sleep(0.1)


if __name__ == "__main__":
    print(datetime.now())
    pool = Pool(8)
    for i in range(100):
        '''
            实际测试发现，for循环内部执行步骤：
            （1）遍历100个可迭代对象，往进程池放一个子进程
            （2）执行这个子进程，等子进程执行完毕，再往进程池放一个子进程，再执行。（同时只执行一个子进程）
            for循环执行完毕，再执行print函数。
            
            For循环中执行步骤：
            （1）循环遍历，将100个子进程添加到进程池（相对父进程会阻塞）
            （2）每次执行8个子进程，等一个子进程执行完后，立马启动新的子进程。（相对父进程会阻塞）
            apply为同步进程池写法。指的是启动子进程的过程，与父进程本身的执行（print）是同步，For循环中往进程池添加子进程的过程，与父进程本身的执行是同步的。
             (3) for循环前执行print test

        '''
        pool.apply(main, args=(i,))  # 维持执行的进程总数为8，当一个进程执行完后启动一个新进程.

    print(f"{datetime.now()} test")  # for循环执行完毕，才会执行此函数
    pool.close()
    pool.join()