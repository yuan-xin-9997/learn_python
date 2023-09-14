"""
Python的threading包主要运用多线程的开发，但由于GIL的存在，Python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，大部分情况需要使用多进程。在Python 2.6版本的时候引入了multiprocessing包，它完整的复制了一套threading所提供的接口方便迁移。唯一的不同就是它使用了多进程而不是多线程。每个进程有自己的独立的GIL，因此也不会出现进程之间的GIL争抢。
借助这个multiprocessing，你可以轻松完成从单进程到并发执行的转换。multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
"""

import os

print('Process (%s) start...' % os.getpid())

# Only works on Unix/Linux/Mac:

pid = os.fork()

if pid == 0:

    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))

else:

    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))