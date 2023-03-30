"""
案例：asyncio + 不支持异步的模块

不支持异步的模块，例如request，
支持异步的：aiohttp

当需要将asyncio和不支持异步的模块在一起使用的时候，为了能够接近异步的
效率，可以使用ayncio+不支持异步的模块+线程池or进程池配合使用，虽然会
消耗更多资源，但能提高效率，不得已而为之

"""
import asyncio
import requests


async def download_image(url):
    # 发送网络请求，下载图片（遇到网络下载图片的IO请求，自动化切换到其他任务）
    print("开始下载:", url)

    loop = asyncio.get_event_loop()
    
    # requests模块默认不支持异步操作，所以就使用线程池来配合实现了。
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print('下载完成')
    # 图片保存到本地文件
    file_name = url.rsplit('_')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    url_list = [
        'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
        'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
    ]

    tasks = [ download_image(url)  for url in url_list]

    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait(tasks) )