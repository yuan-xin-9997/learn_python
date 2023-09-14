# -*- coding: utf-8 -*-

# File Name： 08.multiprocessing_Manager
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:


"""
Manager（用于资源共享）
Manager()返回的manager对象控制了一个server进程，此进程包含的python对象可以被其他的进程通过proxies来访问。从而达到多进程间数据通信且安全。Manager模块常与Pool模块一起使用。
"""
from multiprocessing import Manager, Process


def f(x, arr, l, d, n):

    x.value = 3.14
    arr[0] = 5
    l.append('Hello')
    d[1] = 2
    n.a = 10


if __name__ == '__main__':

    server = Manager()
    x = server.Value('d', 0.0)
    arr = server.Array('i', range(10))
    l = server.list()
    d = server.dict()
    n = server.Namespace()
    print(server.address)

    proc = Process(target=f, args=(x, arr, l, d, n))
    proc.start()
    proc.join()

    print(x.value)
    print(arr)
    print(l)
    print(d)
    print(n)