from functools import wraps
import time


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