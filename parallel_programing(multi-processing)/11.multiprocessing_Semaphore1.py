"""
信号量是一个更高级的锁机制。信号量内部有一个计数器而不像锁对象内部有锁标识，而且只有当占用信号量的线程数超过信号量时线程才阻塞。
这允许了多个线程可以同时访问相同的代码区。比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去，
如果指定信号量为3，那么来一个人获得一把锁，计数加1，当计数等于3时，后面的人均需要等待。一旦释放，就有人可以获得一把锁。
"""
import datetime
from multiprocessing import Process, Semaphore
import time, random


def go_wc(sem, user):
    sem.acquire()
    print(f'{datetime.datetime.now()} %s 占到一个茅坑\n' % user)
    time.sleep(random.randint(2, 3))
    sem.release()
    print(f"{datetime.datetime.now()} ", user, 'OK\n')


if __name__ == '__main__':
    sem = Semaphore(2)  # 可以自行设置信号量的值，观察输出结果
    p_l = []
    for i in range(5):
        p = Process(target=go_wc, args=(sem, 'user%s' % str(i+1),))
        p.start()
        p_l.append(p)

    for i in p_l:
        i.join()