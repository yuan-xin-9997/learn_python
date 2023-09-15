

import time
import os
from multiprocessing import Process, RLock, Lock, Value, Array

"""
RLock（可重入的互斥锁(同一个进程可以多次获得它，同时不会造成阻塞)
RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，
RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，
释放锁时需要调用release()相同次数。可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。
"""
lock = RLock()

"""下面互斥锁，会导致死锁"""
lock = Lock()

def run(lock) -> None:
    fun_A(lock)
    fun_B(lock)

def fun_A(lock):
    lock.acquire()
    print(f'进程{os.getpid()} 函数A加锁1', end='\t')
    lock.acquire()
    print(f'进程{os.getpid()} 函数A加锁2', end='\t')
    time.sleep(0.2)
    lock.release()
    print(f'进程{os.getpid()} 函数A释放1', end='\t')
    lock.release()
    print(f'进程{os.getpid()} 函数A释放2')

def fun_B(lock):
    lock.acquire()
    print(f'进程{os.getpid()} 函数B加锁1', end='\t')
    lock.acquire()
    print(f'进程{os.getpid()} 函数B加锁2', end='\t')
    time.sleep(3)
    lock.release()
    print(f'进程{os.getpid()} 函数B释放1', end='\t')
    lock.release()
    print(f'进程{os.getpid()} 函数B释放2')


if __name__ == '__main__':
    print(f"current process id = {os.getpid()}")

    pa = Process(name="process_A", target=run, args=(lock,))
    pb = Process(name="process_B", target=run, args=(lock,))

    pa.start()
    pb.start()

    pa.join()
    pb.join()