# -*- coding:utf-8 -*-


# wsgi_web_server.py

# from wsgiref.simple_server import make_server
#
# def run_server(environ,response):
#     print(environ)
#
#     response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
#     return [bytes('努力的你真好看', encoding="utf-8")]
#
# s = make_server('localhost',8000,run_server)
# s.serve_forever()  # 注意拼写
# ————————————————————————————————————

# wsgi_web_server_with_urls_img.py
from wsgiref.simple_server import make_server
import re
import os


# BASE_DIR=os.path.abspath()

import os
def book():  # 设置每个页面如何响应
    print('book page')
    # start_response("200 OK",[('Content-type','text/html;charset=utf-8')])
    data = """
            <h1>欢迎来到专区</h1>

                <img src='imgs/testimg.gif' />

            <p>上路飞学城，看尽天下小片</p>
        '''
        """
    return data

def img(request_url):  # 根据图片url，读取图片，返回二进制数据
    if os.path.isfile(request_url):                                 # 如果文件存在
        print('img page')
        request_url = request_url[1:].replace('/', '\\')
        f = open(request_url, 'rb')
        data = f.read()
        return data

def china():
    print('china page')
    data = 'china page'
    return data

def root():
    print('root page')
    data = 'root page'
    return data

def routers():  # 管理每个页面的字典，就是为了方便添加字典，
    urls = {
        '/book': book,
        '/china': china,
        '/': root
    }
    return urls

def run_server(environ, start_response):  # 运行函数
    print(environ)
    url_dict = routers()  # 获取url页面对应对的字典大全
    request_url = environ.get("PATH_INFO")  # 获取请求的页面（内容）的部分url
    print('request url:', request_url)
    start_response("200 OK ", [("Content-type", 'text/html;charset=utf-8')])

    if request_url in url_dict.keys():
        func_data = url_dict[request_url]()  # url_dict[request_url]是路径对应的内容单词，然后其与函数名相同所以直接当作函数名加参数调用
        return [bytes(func_data, encoding='utf-8')]

    elif 'img' in request_url:  # 若有img内的文件的数据则请求 调用函数返回给用户二进制数据流后编码
        return [img(request_url)]

    else:
        # start_response("404 ",[("Content-type",'text/html;charset=utf-8')])
        return [bytes('404 page not found', encoding='utf-8')]


s = make_server('localhost', 8000, run_server)
s.serve_forever()
# 浏览器输入localhost:8000 或+/book   /china



