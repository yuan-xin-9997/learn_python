# -*- coding: utf-8 -*-

# File Name： 05.multiprocessing_queue1
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:
"""
普通的全局变量是不能被子进程所共享的，只有通过Multiprocessing组件构造的数据结构可以被共享。
Queue是用来创建进程间资源共享的队列的类，使用Queue可以达到多进程间数据传递的功能（缺点：只适用Process类，不能在Pool进程池中使用）。
"""
import queue
from multiprocessing import Process, Queue
import os, time, random

def write(q):

    print('Process to write: %s' % os.getpid())

    for value in ['A', 'B', 'C']:

        print('Put %s to queue...' % value)

        q.put(value)

        time.sleep(random.random())

def read(q):

    print('Process to read: %s' % os.getpid())

    while True:

        value = q.get(True)

        print('Get %s from queue.' % value)

if __name__ == "__main__":

    q = Queue()
    # q = queue.Queue()  # 此处必须使用进场process自带Queue，不能使用标准库中queue

    pw = Process(target=write, args=(q,))

    pr = Process(target=read, args=(q,))

    pw.start()

    pr.start()

    pw.join()  # 等待pw结束

    pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止