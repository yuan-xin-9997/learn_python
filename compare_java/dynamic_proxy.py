"""
Python实现Java的动态代理
"""

class User:

    def login(self):
        print('user login')
    def logout(self):
        print('user logout')

class Proxy:
    def __init__(self,target):
        self.target = target

    def __getattribute__(self, name):
        target = object.__getattribute__(self,"target")
        attr = object.__getattribute__(target, name)
        if name == 'login':
            def newFunc(*args, **kwargs):
                print("login start")
                result = attr(*args, **kwargs)
                print("login end")
                return result
            return newFunc
        else:
            return attr

if __name__ == '__main__':
    user = User()
    proxy = Proxy(user)
    proxy.login()
    proxy.logout()