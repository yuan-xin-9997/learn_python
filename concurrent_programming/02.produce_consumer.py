import queue
import produce_consumer_blog_spider
import time
import random
import threading


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = produce_consumer_blog_spider.craw(url)
        html_queue.put(html)

        print(threading.current_thread().name, f" craw {url}", "url_queue.size=", url_queue.qsize(), "\n")
        # time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
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
    
    
    for i in range(10):
        t = threading.Thread(
            target=do_craw, 
            args=(url_queue, html_queue),
            name=f"craw {i}"
        )
        t.start()
    
    fout = open("02.result.txt", "w")
    for j in range(2):
        t = threading.Thread(
            target=do_parse, 
            args=(html_queue, fout),
            name=f"parse {j}"
        )
        t.start()
    