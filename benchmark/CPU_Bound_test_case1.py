import math
import random


def append_to_list(lst, num_items):
    """
    Appends num_items integers within the range [0-20000000) to the input lst
    """
    for n in random.sample(range(20000000), num_items):
        lst.append(n)


def long_time_task(i):
    print("结果: {}".format(8 ** 20))


def is_prime(n):
    """判断一个数是否为素数，CPU密集型计算程序"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True