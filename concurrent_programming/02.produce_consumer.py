import queue
from queue import Empty
import produce_consumer_blog_spider
import time
import random
import threading
"""
演示生产者-消费者模型，10个线程生产，2个线程消费，使用队列在生产者和消费者之间传递数据
https://www.bilibili.com/video/BV1bK411A7tV/
TODO: 无法让程序正常退出
"""

def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        try:
            url = url_queue.get()
        except Empty:
            break
        if url_queue.qsize() == 0:
            break
        html = produce_consumer_blog_spider.craw(url)
        html_queue.put(html)

        print(threading.current_thread().name, f" craw {url}", "url_queue.size=", url_queue.qsize(), "\n")
        # time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    while True:
        try:
            html = html_queue.get()
        except Empty:
            break
        if html_queue.qsize() == 0:
            break
        res = produce_consumer_blog_spider.parse(html)
        for r in res:
            fout.write(str(r) + "\n")

        print(threading.current_thread().name, f" parse {url}", "html_queue.size=", html_queue.qsize(), "\n")
        # time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for url in produce_consumer_blog_spider.urls:
        url_queue.put(url)
    
    c_l = []
    for i in range(10):
        t = threading.Thread(
            target=do_craw, 
            args=(url_queue, html_queue),
            name=f"craw {i}"
        )
        c_l.append(t)
        t.start()
    
    fout = open("02.result.txt", "w")
    p_l = []
    for j in range(2):
        t = threading.Thread(
            target=do_parse,
            args=(html_queue, fout),
            name=f"parse {j}"
        )
        p_l.append(t)
        t.start()


    # TODO：添加之后还是无法退出
    for t in c_l:
        t.join()

    for t in p_l:
        t.join()
