# -*- coding: utf-8 -*-

# File Name： 04.multiprocessing_pool3
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:

# 异步进程池（非阻塞）
import os
from multiprocessing import Pool

def main(i):

    print(f"current pid = {os.getpid()}, the value = {i}")

if __name__ == "__main__":

    pool = Pool(8)

    for i in range(100):

        '''

            实际测试发现，for循环内部执行步骤：

            （1）遍历100个可迭代对象，往进程池放一个子进程
            （2）执行这个子进程，等子进程执行完毕，再往进程池放一个子进程，再执行。（同时只执行一个子进程）

            for循环执行完毕，再执行print函数。

        '''

        pool.apply(main, args=(i,))  # 维持执行的进程总数为8，当一个进程执行完后启动一个新进程.

    print("test")

    pool.close()

    pool.join()