"""
此程序对比CPU密集型程序，使用单线程、多线程、多进程方式进行计算
性能：多线程>单线程>多线程
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from functools import wraps

a = 11293754244211231
numbers = [a + i for i in range(1, 1001)]
numbers.insert(0, 2)


def time_this(func):
    """统计函数func的运行时间"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('函数{}.{}运行时间 : {} 秒'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


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


@time_this
def single_thread():
    """单线程计算程序"""
    res = []
    for number in numbers:
        # print(is_prime(number))
        is_prime(number)
        # res.append(is_prime(number))
    # print(res)


@time_this
def multi_thread():
    """多线程计算程序"""
    with ThreadPoolExecutor() as pool:
        res = pool.map(is_prime, numbers)
    # print(list(res))


@time_this
def multi_process():
    """多进程计算程序"""
    with ProcessPoolExecutor() as pool:
        res = pool.map(is_prime, numbers)
    # print(list(res))


if __name__ == '__main__':
    print(numbers)
    single_thread()
    multi_thread()
    multi_process()
