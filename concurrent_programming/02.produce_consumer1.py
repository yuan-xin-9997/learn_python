# -*- coding: utf-8 -*-

# File Name： 02.produce_consumer1
# Description :
# Author : yuan.xin
# create_date： 2023/9/12
# Change Activity:
"""
演示生产者-消费者模型，10个线程生产，2个线程消费，使用队列在生产者和消费者之间传递数据
https://www.bilibili.com/video/BV1bK411A7tV/
通过异常处理和队列get超时机制让多线程程序正常退出
"""


import queue
from queue import Empty
import produce_consumer_blog_spider
import threading

def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        try:
            # url = url_queue.get()  # 使用超时来避免无限阻塞
            url = url_queue.get(timeout=1)  # 使用超时来避免无限阻塞，关键是timeout=1，以及try except能够让程序进行退出
            # if url is None:  # 检查哨兵值以退出
            #     break
        except Empty:
            break
        html = produce_consumer_blog_spider.craw(url)
        html_queue.put(html)

        print(threading.current_thread().name, f" craw {url}", "url_queue.size=", url_queue.qsize(), f"html_queue.qsize={html_queue.qsize()}", "\n")

def do_parse(html_queue: queue.Queue, fout):
    while True:
        try:
            # html = html_queue.get()  # 使用超时来避免无限阻塞
            html = html_queue.get(timeout=1)  # 使用超时来避免无限阻塞
            # if html is None:  # 检查哨兵值以退出
            #     break
        except Empty:
            break
        # html = html_queue.get(timeout=1)  # 使用超时来避免无限阻塞
        res = produce_consumer_blog_spider.parse(html)
        # print("res=", res)
        for r in res:
            fout.write(str(r) + "\n")

        print(threading.current_thread().name, f" parse {url}", "html_queue.size=", html_queue.qsize(), "\n")


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

    # 通知线程退出
    # for _ in c_l:
    #     url_queue.put(None)
    # for _ in p_l:
    #     html_queue.put(None)

    # 等待所有线程完成
    for t in c_l:
        t.join()
    for t in p_l:
        t.join()

    # 使用with语句来关闭输出文件以确保资源清理
    with fout:
        print("所有线程都已完成。退出程序。")
