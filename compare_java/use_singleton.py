import singleton
from singleton import *
if __name__ == '__main__':
    print(singleton.instance.name)
    instance = Singleton()