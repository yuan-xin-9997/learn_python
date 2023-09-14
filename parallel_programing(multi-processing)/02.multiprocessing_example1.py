"""
多进程案例

建管理进程模块：
Process（用于创建进程）
Pool（用于创建管理进程池）
Queue（用于进程通信，资源共享）
Value，Array（用于进程通信，资源共享）
Pipe（用于管道通信）
Manager（用于资源共享）

同步子进程模块：
Condition（条件变量）
Event（事件）
Lock（互斥锁）
RLock（可重入的互斥锁(同一个进程可以多次获得它，同时不会造成阻塞)
Semaphore（信号量）
"""

from multiprocessing import Process
import os

def run_proc(name):

    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':

    print('Parent process %s.' % os.getpid())

    p = Process(target=run_proc, args=('test',))

    print('Child process will start.')

    p.start()

    p.join()

    print('Child process end.')