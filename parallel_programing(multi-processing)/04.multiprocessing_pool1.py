"""
Pool（用于创建管理进程池），案例

Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，就重用进程池中的进程。
构造方法：Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
processes ：要创建的进程数，如果省略，将默认使用cpu_count()返回的数量。
initializer：每个工作进程启动时要执行的可调用对象，默认为None。如果initializer是None，那么每一个工作进程在开始的时候会调用initializer(*initargs)。
initargs：是要传给initializer的参数组。
maxtasksperchild：工作进程退出之前可以完成的任务数，完成后用一个新的工作进程来替代原进程，来让闲置的资源被释放。maxtasksperchild默认是None，意味着只要Pool存在工作进程就会一直存活。
context: 用在制定工作进程启动时的上下文，一般使用Pool() 或者一个context对象的Pool()方法来创建一个池，两种方法都适当的设置了context。

实例方法
map(func, iterable[, chunksize=None])：Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到返回结果。注意，虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。
"""
import os
from multiprocessing import Pool

def main(i):
    print(f"current pid = {os.getpid()}, the value = {i}")


if __name__ == "__main__":

    lists = range(100)

    pool = Pool(8)

    pool.map(main, lists)

    pool.close()

    pool.join()