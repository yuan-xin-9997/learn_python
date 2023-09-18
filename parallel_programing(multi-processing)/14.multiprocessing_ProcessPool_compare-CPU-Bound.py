"""
ref Python两种多进程方式的内存开销 - IMIser的文章 - 知乎
https://zhuanlan.zhihu.com/p/588189685

随着PC和服务器cpu都朝着多核发展，除了一些不太追求极限的场景（web server），python程序的优化都可以直接无脑上多进程。从而不用分析CPython的多线程啥时候work啥时候不管用。

但是Python的多进程官方提供了多个接口：
原始的`multiprocessing.Process`
进程池 `multiprcocessing.Pool`
进程池 `concurrent.futures.ProcessPoolExecutor`
我们看看在大内存需求场景下，三者有无区别（比如你要并行读一个很大的文件），测试代码

这是一个CPU密集型的程序
"""

import os
# import numpy as np
import time
from multiprocessing import Process
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from memory_profiler import profile
from benchmark import append_to_list
# append_to_list([], 10000000)

class Benchmark:
    def __init__(self, text):
        self.text = text
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, *args):
        self.end = time.time()
        print("%s: consume: %s" % (self.text, self.end - self.start))

#main data source
worker_num = os.cpu_count()


# 1. multiprocessing.Porcess
@profile
def loop_mp():
    pool = []
    for i in range(worker_num):
        p = Process(target=append_to_list, args=([], 10000000))
        p.start()
        pool.append(p)
    for p in pool:
        p.join()

# 3. multiprocessing.Pool
@profile
def mp_pool():
    with Pool(processes=worker_num) as pool:
        tasks = []
        for i in range(worker_num):
            tasks.append(
                pool.apply_async(append_to_list, args=([], 10000000))
            )
        pool.close()
        pool.join()

# 4. ProcessPoolExecutor
@profile
def loop_pool():
    with ProcessPoolExecutor(max_workers=worker_num) as exe:
        for i in range(worker_num):
            exe.submit(
                # target=append_to_list, args=([], 10000000)
                append_to_list, [], 10000000
            )

# 6.  direct
@profile
def direct():
    for i in range(worker_num):
        append_to_list([], 10000000)


if __name__ == '__main__':
    print("当前环境CPU核数: ", worker_num)
    with Benchmark("循环创建进程"):
        print("循环创建进程")
        loop_mp()
    print()
    with Benchmark("使用multiprocessing的Pool进程池"):
        print("使用multiprocessing的Pool进程池")
        mp_pool()
    print()
    with Benchmark("使用concurrent.futures的ProcessPoolExecutor进程池"):
        print("使用concurrent.futures的ProcessPoolExecutor进程池")
        loop_pool()
    print()
    with Benchmark("使用单进程"):
        print("使用单进程")
        direct()