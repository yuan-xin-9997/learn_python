# -*- coding: utf-8 -*-

# File Name： __init__.py
# Description :
# Author : yuanxin
# create_date： 2023/9/26
# Change Activity:
import time

def time_this(func, *args, **kwargs):
    start = time.perf_counter()
    r = func(*args, **kwargs)
    end = time.perf_counter()
    print('函数{}.{}运行时间 : {} 秒'.format(func.__module__, func.__name__, end - start))
    return r


def main(name):
    for i in range(1000000):
        print(i)
    print(f"hello, {name}")


if __name__ == '__main__':
    time_this(
        main, "Vitas"
    )
    # main()