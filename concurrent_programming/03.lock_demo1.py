import threading
import time


class Account:

    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    if account.balance >= amount:
        time.sleep(0.1)  # 由于sleep会发生线程阻塞，导致线程切换，因此执行结果一定是错误的
        print(
            threading.current_thread().name, "取钱成功"
        )
        account.balance -= amount
        print(
            threading.current_thread().name, f"余额{account.balance}"
        )
    else:
       print(
            threading.current_thread().name, "取钱失败，余额不足"
        )


if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(
        name="ta",
        target=draw,
        args=(account, 800)
    )
    tb = threading.Thread(
        name="tb",
        target=draw,
        args=(account, 800)
    )

    ta.start()
    tb.start()