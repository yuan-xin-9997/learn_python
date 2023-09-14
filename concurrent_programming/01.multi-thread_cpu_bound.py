"""
演示多线程与单线程在CPU密集型程序的性能对比

"""
import threading

from benchmark import append_to_list
from util import time_this

NUM_PROC = 4
"""
函数__main__.cpu_bound_func_without_multithread运行时间 : 71.35722390000001 秒
函数__main__.cpu_bound_func_with_multithread运行时间 : 71.17269610000001 秒
"""

@time_this
def cpu_bound_func_without_multithread():
    for i in range(NUM_PROC):
        append_to_list([], 10000000)

@time_this
def cpu_bound_func_with_multithread():
    threads = []
    for t in range(NUM_PROC):
        threads.append(
            threading.Thread(target=append_to_list, args=([], 10000000))
        )

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    cpu_bound_func_without_multithread()
    cpu_bound_func_with_multithread()
