"""
greenlet实现协程，即一个线程在多个函数之间切换
"""

from greenlet import greenlet

def func1():
    print(1) #第 1 步：输出 1
    gr2.switch() #第 3 步：切换到 func2 函数，       模拟IO阻塞，手动切换
    print(2) #第 6 步：输出 2
    gr2.switch() #第 7 步：切换到 func2 函数，从上一次执行的位置继续向后执行

def func2():
    print(3) #第 4 步：输出 3
    gr1.switch() #第 5 步：切换到 func1 函数，从上一次执行的位置继续向后执行
    print(4) #第 8 步：输出 4


gr1 = greenlet(func1) 
gr2 = greenlet(func2)
gr1.switch() #第 1 步：去执行 func1 函数