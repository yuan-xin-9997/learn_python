# is
# ==
# id()

"""

## 关于Python 可变对象和不可变对象的区别
python内置的一些类型中
可变对象：list dict set
不可变对象：tuple string int float bool
可变对象是可以直接被改变的，可变对象改变之后（比如往list、dict、set增加或删除元素），其id输出的内存地址不会发生改变，即其内存地址不变
而不可变对象则不可以，如果对不可变对象重新赋值，会生成一个新的对象或抛出类型错误

## 关于Python is 和 == 的区别

 is 表示的是对象标示符（object identity），而 == 表示的是相等（equality）。is 的作用是用来检查对象的标示符是否一致，
 也就是比较两个对象在内存中的地址是否一样，而 == 是用来检查两个对象是否相等。我们在检查 a is b 的时候，其实相当于检查 id(a) == id(b)。
 而检查 a == b 的时候，实际是调用了对象 a 的 __eq()__ 方法，a == b 相当于 a.__eq__(b)。
 一般情况下，如果 a is b 返回True的话，即 a 和 b 指向同一块内存地址的话，a == b 也返回True，即 a 和 b 的值也相等。

is 是检查两个对象是否指向同一块内存空间，而 == 是检查他们的值是否相等。可以看出，is 是比 == 更严格的检查，is 返回True表明这两个对象指向同一块内存，值也一定相同。

## 关于Python 的id()函数
id() 函数返回对象的唯一标识符，标识符是一个整数。
CPython 中 id() 函数用于获取对象的内存地址。
官方解释：
Return the identity of an object.
This is guaranteed to be unique among simultaneously existing objects.
(CPython uses the object's memory address.)

hex()函数，返回一个十进制数的十六进制
Return the hexadecimal representation of an integer.
hex(12648430)
'0xc0ffee'

## 重新自定义类的__eq__方法
"""

print("1=============================")

a: str = "hello"
b = "hello"
print(a is b)  # 输出 True
print(a == b)  # 输出 True

print("2=============================")

a = "hello world"
b = "hello world"
print(a is b)  # 输出 True
print(a == b)  # 输出 True

print("3=============================")

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # 输出 False
print(a == b)  # 输出 True

print("4=============================")

a = [1, 2, 3]
b = a
print(a is b)  # 输出 True
print(a == b)  # 输出 True

print("5=============================")

a = "hello"
b = "hello"
print(id(a))   # 输出 140506224367496
print(id(b))   # 输出 140506224367496
print(a is b)  # 输出 True
print(a == b)  # 输出 True

print("6=============================")

a = "hello world 由于Python缓存了整数和短字符串，因此每个对象只存有一份。比如，所有整数1的引用都指向同一对象。即使使用赋值语句，也只是创造了新的引用，而不是对象本身。长的字符串和其它对象可以有多个相同的对象，可以使用赋值语句创建出新的对象"
b = "hello world 由于Python缓存了整数和短字符串，因此每个对象只存有一份。比如，所有整数1的引用都指向同一对象。即使使用赋值语句，也只是创造了新的引用，而不是对象本身。长的字符串和其它对象可以有多个相同的对象，可以使用赋值语句创建出新的对象"
print(id(a))   # 输出 140506208812208
print(id(b))   # 输出 140506208812208
print(a is b)  # 输出 True
print(a == b)  # 输出 True

print("7=============================")

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))   # 输出 140506224299464
print(id(b))   # 输出 140506224309576
print(a is b)  # 输出 False
print(a == b)  # 输出 True

print("8=============================")

a = [1, 2, 3]
b = a
print(id(a))   # 输出 140506224305672
print(id(b))   # 输出 140506224305672
print(a is b)  # 输出 True
print(a == b)  # 输出 True

print("9=============================")

a = 1
b = 1
print(id(a))
print(id(b))
print(a == b)
print(a is b)

a = (1, 2)
b = (1, 2)
c = (1, 2)
print(id(a))
print(id(b))
print(id(c))
print(a == b)
print(a is b)

print("10=============================")
a = {"a": 123}
b = {"a": 123}
print(id(a))
print(id(b))
print(a == b)
print(a is b)

print("11=============================")
# 可变对象：list dict set
# 可变对象是可以直接被改变的，可变对象改变之后（比如往list、dict、set增加或删除元素），其id输出的内存地址不会发生改变，即变量指向的内存地址不变
a = [1, 2, 3]
print(id(a))
a.append(4)
print(a)
print(id(a))
a.remove(1)
print(a)
print(id(a))

print("12=============================")

# 不可变对象：tuple string int float bool
a = "hello"
b= "hello"
print(id(a))
a = a+" world"
print(id(a))  # 当对string对象重新赋值的时候，其实是让变量指向另一个内存地址，原来的"hello"依然还在原来的内存中
print(id(b))

# a[0] = "L"  # # 对不可变对象进行改变的时候TypeError: 'str' object does not support item assignment
# print(a)

# a = (1,2,3)
# a[1]=2  # 对不可变对象进行改变的时候，会引发TypeError: 'tuple' object does not support item assignment

print("13=============================")
a = 1
print(id(a))  # 变量a的内存地址（十进制）
print(hex(id(a)))  # 变量a的内存地址（十六进制）

print("14=============================")
class MyDataStructure:

    def __eq__(self, other):  # 重新自定义类的__eq__方法，当对自定义类进行比较的时候，会优先调用此方法
        return True
        # print("compare")
        # return self is other


a = MyDataStructure()
b = 1
print(id(a))
print(id(b))
print(a==b)  # True
print(b == a)  # True
print(a is b)  # Fals
