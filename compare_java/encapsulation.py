"""
Python的封装，伪私有


"""

class Person:
    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__age = 10
    # 私有方法
    def __secret(self):
        return self.__age

p = Person("andy")
print(p.name)  # 可以访问

"""
下面代码会报错
D:\miniconda3\python.exe D:\dev\learn_python\compare_java\encapsulation.py 
Traceback (most recent call last):
  File "D:\dev\learn_python\compare_java\encapsulation.py", line 18, in <module>
    print(p.__age)  # 私有屬性，无法坊问
          ^^^^^^^
AttributeError: 'Person' object has no attribute '__age'
andy
"""
# print(p.__age)  # 私有屬性，无法坊问
# print(p.__secret())  #私有方法，无法访问


# 但是可以通过以下方式访问，这也就为什么说Python是伪私有的属性和方法
print(p._Person__age)
print(p._Person__secret())