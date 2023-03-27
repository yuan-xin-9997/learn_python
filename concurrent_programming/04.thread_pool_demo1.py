import concurrent.futures
import blog_spider
import time
import produce_consumer_blog_spider


# TODO: 为何会报TypeError

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    print(htmls)
    time.sleep(1)
    for url, html in htmls:
        try:
            print(url, len(html))
        except TypeError:
            continue

print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(produce_consumer_blog_spider.parse, html)
        futures[future] = url

    print(futures)

    # for future, url in futures.items():
    #     try:
    #         print(url, future.result())
    #     except TypeError:
    #         continue

    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        try:
            print(url, future.result()) 
        except TypeError:
            print("error")
            continue

print("parse over")