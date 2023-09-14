import threading
import time

"""
演示多线程同步，同一个线程重复获取互斥锁会导致死锁的情况
用以对比 可重入的互斥锁(同一个进程可以多次获得它，同时不会造成阻塞），同一个线程获取RLOCK不会出现死锁的情况
"""

lock = threading.RLock()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.fun_A()
        self.fun_B()

    def fun_A(self):
        lock.acquire()
        print(f'线程{threading.current_thread().name} 函数A加锁1', end='\t')
        lock.acquire()
        print(f'线程{threading.current_thread().name} 函数A加锁2', end='\t')
        time.sleep(0.2)
        lock.release()
        print(f'线程{threading.current_thread().name} 函数A释放1', end='\t')
        lock.release()
        print(f'线程{threading.current_thread().name} 函数A释放2')

    def fun_B(self):
        lock.acquire()
        print(f'线程{threading.current_thread().name} 函数B加锁1', end='\t')
        lock.acquire()
        print(f'线程{threading.current_thread().name} 函数B加锁2', end='\t')
        time.sleep(3)
        lock.release()
        print(f'线程{threading.current_thread().name} 函数B释放1', end='\t')
        lock.release()
        print(f'线程{threading.current_thread().name} 函数B释放2')


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()