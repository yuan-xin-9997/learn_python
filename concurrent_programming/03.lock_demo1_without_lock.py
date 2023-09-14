import threading
import time

"""
演示多线程同步中的锁机制（没有加锁的案例）
在本案例中，创建两个线程，两个线程需要访问共享数据account
在线程内部的执行的方法draw中，由于有sleep，会发生线程切换，导致两个线程在开始读取的余额都是1000
"""

class Account:

    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    if account.balance >= amount:
        print(
            threading.current_thread().name, f"取钱之前，余额{account.balance}"
        )
        time.sleep(0.1)  # 由于sleep会发生线程阻塞，模拟IO场景，导致线程切换，因此执行结果一定是错误的
        print(
            threading.current_thread().name, "取钱成功"
        )
        account.balance -= amount
        print(
            threading.current_thread().name, f"取钱之后，余额{account.balance}"
        )
    else:
       print(
            threading.current_thread().name, "取钱失败，余额不足"
        )


if __name__ == "__main__":
    print("当前线程 =", threading.current_thread().name)
    account = Account(1000)
    ta = threading.Thread(
        name="thread_a",
        target=draw,
        args=(account, 800)
    )
    tb = threading.Thread(
        name="thread_b",
        target=draw,
        args=(account, 800)
    )

    ta.start()
    tb.start()