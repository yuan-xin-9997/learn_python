# -*- coding: utf-8 -*-

# File Name： 06.multiprocessing_Value_Array
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:
"""
multiprocessing 中Value和Array的实现原理都是在共享内存中创建ctypes()对象来达到共享数据的目的，两者实现方法大同小异，只是选用不同的ctypes数据类型而已。
注意：Value和Array只适用于Process类。
"""
import multiprocessing

def f(n, a):

    n.value = 3.14

    a[0] = 5

if __name__ == '__main__':

    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))

    p = multiprocessing.Process(target=f, args=(num, arr))

    p.start()

    p.join()

    print(num.value)

    print(arr[:])