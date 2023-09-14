

from benchmark import append_to_list
import multiprocessing
from util import time_this

# NUM_PROC = 4
"""
函数__main__.cpu_bound_func_without_multiprocessing运行时间 : 69.31169080000001 秒
函数__main__.cpu_bound_func_with_multiprocessing运行时间 : 31.854890400000002 秒
"""
NUM_PROC = 2
"""
函数__main__.cpu_bound_func_without_multiprocessing运行时间 : 37.636348600000005 秒
函数__main__.cpu_bound_func_with_multiprocessing运行时间 : 21.655044600000004 秒
"""


@time_this
def cpu_bound_func_without_multiprocessing():
    for i in range(NUM_PROC):
        append_to_list([], 10000000)

@time_this
def cpu_bound_func_with_multiprocessing():
    jobs = []

    for i in range(NUM_PROC):
        process = multiprocessing.Process(
            target=append_to_list,
            args=([], 10000000)
        )
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()


if __name__ == "__main__":
    cpu_bound_func_without_multiprocessing()
    cpu_bound_func_with_multiprocessing()

