"""
ref: https://zhuanlan.zhihu.com/p/137649301

一、什么是Requests

Requests 是⽤Python语⾔编写，基于urllib，采⽤Apache2 Licensed开源协议的 HTTP 库。它⽐ urllib 更加⽅便，可以节约我们⼤量的⼯作，完全满⾜HTTP测试需求。

⼀句话——Python实现的简单易⽤的HTTP库

二、安装Requests库
进入命令行win+R执行

命令：pip install requests

项目导入：import requests
"""

# 三、各种请求方式
# 直接上代码，不明白可以查看我的urllib的基本使用方法
import requests
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')
# 这么多请求方式，都有什么含义，所以问下度娘：
#
# GET： 请求指定的页面信息，并返回实体主体。
#
# HEAD： 只请求页面的首部。
#
# POST： 请求服务器接受所指定的文档作为对所标识的URI的新的从属实体。
#
# PUT： 从客户端向服务器传送的数据取代指定的文档的内容。
#
# DELETE： 请求服务器删除指定的页面。
#
# get 和 post比较常见 GET请求将提交的数据放置在HTTP请求协议头中；POST提交的数据则放在实体数据中

# （1）、基本的GET请求
# response = requests.get('http://httpbin.org/get')
response = requests.get('http://www.baidu.com/')
print(response.headers)
print(response.text)


# （2）、带参数的GET请求
# 将name和age传进去
response = requests.get("http://httpbin.org/get?name=germey&age=22")
print(response.headers)
print(response.text)

# 或者使用params的方法：
data = {
    'name': 'germey',
    'age': 22
}
response = requests.get("http://httpbin.org/get", params=data)
print(response.text)







