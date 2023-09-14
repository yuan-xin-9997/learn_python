# -*- coding: utf-8 -*-

# File Name： 05.multiprocessing_JoinableQueue1
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:

"""
JoinableQueue就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。
构造方法：JoinableQueue([maxsize])
maxsize：队列中允许最大项数，省略则无大小限制。
实例方法
JoinableQueue的实例p除了与Queue对象相同的方法之外还具有：
task_done()：使用者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常
join():生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止
"""

from multiprocessing import Process, JoinableQueue

import time, random

def consumer(q):

    while True:

        res = q.get()

        print('消费者拿到了 %s' % res)

        q.task_done()

def producer(seq, q):

    for item in seq:

        time.sleep(random.randrange(1,2))

        q.put(item)

        print('生产者做好了 %s' % item)

    q.join()

if __name__ == "__main__":

    q = JoinableQueue()

    seq = ('产品%s' % i for i in range(5))

    p = Process(target=consumer, args=(q,))

    p.daemon = True  # 设置为守护进程，在主线程停止时p也停止，但是不用担心，producer内调用q.join保证了consumer已经处理完队列中的所有元素

    p.start()

    producer(seq, q)

    print('主线程')