# -*- coding: utf-8 -*-

# File Name： 04.multiprocessing_mp_Pool4_apply_async_map
# Description :
# Author : yuan.xin
# create_date： 2023/9/18
# Change Activity:


"""
Python进程池常用的方法  ref https://zhuanlan.zhihu.com/p/46368084

1.apply_async

函数原型：apply_async(func[, args=()[, kwds={}[, callback=None]]])

其作用是向进程池提交需要执行的函数及参数， 各个进程采用非阻塞（异步）的调用方式，即每个子进程只管运行自己的，不管其它进程是否已经完成。这是默认方式。

2.map()

函数原型：map(func, iterable[, chunksize=None])

Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回。 注意：虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。

3.map_async()

函数原型：map_async(func, iterable[, chunksize[, callback]])
与map用法一致，但是它是非阻塞的。其有关事项见apply_async。

4.close()

关闭进程池（pool），使其不在接受新的任务。

5. terminate()

结束工作进程，不在处理未处理的任务。

6.join()

主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。


map 和 map_async 入参为迭代器类型，可以批量调用。而apply和apply_async只能一个个调用。

对于apply_async(func,args)，func为要执行任务的函数名，args为一个列表或元组这样的可迭代对象，里面包含的是要传递给func的参数，对于多个子任务，要分别多次调用apply_async()一一添加，不过这可以通过列表解析实现，以让多个进程的结果返回保存在一个列表中。而对于map_async(func,iterable,chunksize)，如果多个子任务通过同一函数执行，只是参数不同，那么可以把拆分后的参数以列表形式通过iterable传入，并通过chunksize参数指定进程数（实际上这里的chunksize表示的是对iterable的拆分数，但最好让其等于进程数），这样就不需要一一添加。

以上只是两者细微的差别，更重要的差别在于，若是通过apply_async()方法，由于是手动指定进程并添加任务，这样每个进程的执行结果之间是独立的，会分别保存，这样的好处在于，尽管可能其中某几个进程出现了错误，抛出异常，但是并不会导致其他的进程也失败，其他的进程并不会受影响，而且当获取这个抛出异常的进程的结果时，还会返回异常信息；但是如果是map_async()方法，其子参数任务并不是独立的，如果其中的某个子参数任务抛出异常，同时也会导致其他的子参数任务停止，也就是说，并不是通过独立线程来执行不同的子参数任务的。

通过上述的对比，可知当拆分任务一提高执行效率时，通过列表解析使用apply_async()方法添加子任务，使用独立多进程去执行是比map_async()方法更好的，因此这种情况下，apply_async()是最优选择。
"""
from util import time_this
from multiprocessing import Pool, cpu_count
import os
import time


def long_time_task(i):
    # print('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


@time_this
def direct():
    for i in range(5):
        long_time_task(i)

@time_this
def apply_method():
    p = Pool(4)
    for i in range(5):
        p.apply(long_time_task, args=(i,))
    print('等待所有子进程完成。')
    p.close()
    p.join()

@time_this
def async_apply_method():
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子进程完成。')
    p.close()
    p.join()


@time_this
def map_method():
    p = Pool(4)
    inp = []
    for i in range(5):
        inp.append(i)
    p.map(long_time_task, inp)
    print('等待所有子进程完成。')
    p.close()
    p.join()


@time_this
def map_async_method():
    p = Pool(4)
    inp = []
    for i in range(5):
        inp.append(i)
    p.map_async(long_time_task, inp)
    print('等待所有子进程完成。')
    p.close()
    p.join()


def main():
    direct()
    apply_method()
    async_apply_method()
    map_method()
    map_async_method()


if __name__=='__main__':
    print('当前母进程: {}'.format(os.getpid()))
    main()
