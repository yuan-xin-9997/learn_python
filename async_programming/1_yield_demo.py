"""
使用yeild关键字实现线程，即一个线程在多个函数之间切换
"""

def func1():
    yield 1
    yield from func2()  # 模拟IO阻塞
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    print(item)