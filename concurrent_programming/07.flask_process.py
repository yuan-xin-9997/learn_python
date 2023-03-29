"""
本程序演示使用多进程的Flask web服务
"""

import math
import json
from concurrent.futures import ProcessPoolExecutor
import flask

app = flask.Flask(__name__)


def is_prime(n):
    """判断一个数是否为素数，CPU密集型计算程序"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    res = process_pool.map(is_prime, number_list)
    return json.dumps(
        dict(zip(number_list, res))
    )


if __name__ == '__main__':
    process_pool = ProcessPoolExecutor()
    app.run()
