"""
Python实现反射

在 Java 帝国，人们经常通过反射的方式來快取一个类的屬性和方法，之后根据一个字
符串的名称来调用某个类的方法。

比如有个URL为hser?action=[ogin,系统先根据约定解析它，确定类是 User,方法是
login,然后可以创建 User 对象，通过反射调用 togin方法。
public class User{
    public void login(...){
        ...
    }



Python
ref https://www.runoob.com/python/python-func-globals.html
globals() 函数会以字典类型返回当前位置的全部全局变量。

"""
import copy
from types import FunctionType


class User:
    def login(self):
        print("login")


methods = [ x for x,y in User.__dict__.items() if type(y) == FunctionType]
print(methods)

clz = "User"
action = "login"

# 根据名称获得User对象的方法
user = globals()[clz]()
func = getattr(user, action)  # 获取login方法
func()

# print(globals())
globall = copy.copy(globals())
for key,value in globall.items():
    print(key, value)