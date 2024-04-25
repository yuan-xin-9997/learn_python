import sys
import foo

a = [1, 'python']
a = 'a string'

def func():
    a = 1
    b = 257
    print(a + b)

print(a)

if __name__ == '__main__':
    func()
    foo.add(1, 2)

    for k, v in sys.modules.items():
        print(k, v)