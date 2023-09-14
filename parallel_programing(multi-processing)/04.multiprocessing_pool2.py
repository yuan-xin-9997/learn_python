# -*- coding:utf-8 -*-
import os
# 异步进程池（非阻塞）

from multiprocessing import Pool

def main(i):
    print(f"current pid = {os.getpid()}, the value = {i}")

if __name__ == "__main__":

    pool = Pool(8)

    for i in range(100):

        '''
        For循环中执行步骤：
        （1）循环遍历，将100个子进程添加到进程池（相对父进程会阻塞）
        （2）每次执行8个子进程，等一个子进程执行完后，立马启动新的子进程。（相对父进程不阻塞）
        apply_async为异步进程池写法。异步指的是启动子进程的过程，与父进程本身的执行（print）是异步的，而For循环中往进程池添加子进程的过程，与父进程本身的执行却是同步的。
         (3) for循环前执行print test
        '''

        pool.apply_async(main, args=(i,))  # 维持执行的进程总数为8，当一个进程执行完后启动一个新进程.

    print("test")

    pool.close()

    pool.join()