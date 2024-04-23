# builtins，内置模块的命名空间。Python 在启动的时候会自动为我们载入很多内置的函数、类，比如 dict，list，type，print，这些都位于 __builtins__ 模块中，可以使用 dir(__builtins__) 来查看。这也是为什么我们在没有 import 任何模块的情况下，就能使用这么多丰富的函数和功能了。
import sys
from sys import intern

print(dir(__builtins__))
built = dir(__builtins__)
for i in built:
    print(i)

# 2.12 内置属性 __name__
# 现在到了解释 if __name__ == '__main__' 这行代码的时候了。当 Python 程序启动后，Python 会自动为每个模块设置一个属性 __name__ 通常使用的是模块的名字，也就是文件名，但唯一的例外是主模块，
# 主模块将会被设置为 __main__。利用这一特性，就可以做一些特别的事。比如当该模块以主模块来运行的时候，可以运行测试用例。而当被其他模块 import 时，则只是乖乖的，提供函数和功能就好。
print(__name__)

# 3.2 小整数对象池
# 在 demo.py 这里例子中，所用的整数特意用了一个 257，这是为了介绍小整数对象池的。整数在程序中的使用非常广泛，Python 为了优化速度，使用了小整数对象池，避免为整数频繁申请和销毁内存空间。
#
# Python 对小整数的定义是 [-5, 257)，这些整数对象是提前建立好的，不会被垃圾回收。在一个 Python 的程序中，所有位于这个范围内的整数使用的都是同一个对象，从下面这个例子就可以看出。
a = 1
print(id(a))
b = 1
print(id(b))

c = 2580
print(id(c))
d = 2580
print(id(d))
# todo: 此处c和d的id都是相同的？？？？

# 对于大整数，Python 使用的是一个大整数对象池。这句话的意思是：
# 每当创建一个大整数的时候，都会新建一个对象，但是这个对象不再使用的时候，并不会销毁，后面再建立的对象会复用之前已经不再使用的对象的内存空间。（这里的不再使用指的是引用计数为0，可以被销毁）

# 3.3 字符串对象缓冲池
# 如果仔细思考一下，一定会猜到字符串也采用了这种类似的技术，我们来看一下
a = 'a'
b = 'a'
print(id(a))
print(id(b))

a = 'a string of'
b = 'a string of'
print(a is b)
a = intern('a string')  # 手动调用 intern 方法
b = intern('a string')
print(a is b)

# 3.4 import 指令
# 前文提到 import 指令是用来载入 module 的，如果需要，也会顺道做编译的事。但 import 指令，还会做一件重要的事情就是把 import 的那个 module 的代码执行一遍，这件事情很重要。Pytho
# n 是解释执行的，连函数都是执行的时候才创建的。如果不把那个 module 的代码执行一遍，那么 module 里面的函数都没法创建，更别提去调用这些函数了。
#
# 执行代码的另外一个重要作用，就是在这个 module 的命名空间中，创建模块内定义的函数和各种对象的符号名称（也就是变量名），并将其绑定到对象上，
# 这样其他 module 才能通过变量名来引用这些对象。
#
# Python 虚拟机还会将已经 import 过的 module 缓存起来，放到一个全局 module 集合 sys.modules 中。这样做有一个好处，即如果程序的在另一
# 个地方再次 import 这个模块，Python 虚拟机只需要将全局 module 集合中缓存的那个 module 对象返回即可。
#
# 你现在一定想到了 sys.modules 是一个 dict 对象，可以通过 type(sys.modules) 来验证
print(type(sys.modules))
print(sys.modules)

