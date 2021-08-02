# -*-coding: utf-8 -*-
from time import sleep
import threading

__author__ = 'pb'

import http.client
from tornado.httpserver import HTTPServer
from socketserver import ThreadingMixIn
import tornado
import tornado.ioloop
import tornado.web
from tornado.ioloop import IOLoop

port = 8899
import urllib.parse

def request(url, cookie=''):
    ret = urllib.parse.urlparse(url)    # Parse input URL
    if ret.scheme == 'http':
        conn = http.client.HTTPConnection(ret.netloc)
    elif ret.scheme == 'https':
        conn = http.client.HTTPSConnection(ret.netloc)

    url = ret.path
    if ret.query: url += '?' + ret.query
    if ret.fragment: url += '#' + ret.fragment
    if not url: url = '/'

    conn.request(method='GET', url=url , headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
    return conn.getresponse()

class MyRequestHandler(tornado.web.RequestHandler):
    def get(self,requests):
        try:
            self.path = self.request.uri
            print(self.path)
            cur_thread = threading.currentThread()
            print("thread {}".format(cur_thread))
            self.set_header("Content-Type","text/html; charset=gbk")
            retbody = request("{}{}".format('https://bbs.byr.cn',str(self.path))).read()
            self.write(retbody) 
        except:
            import traceback
            traceback.print_exc()

def make_app():
    return tornado.web.Application([
        (r"/(.*)", MyRequestHandler),
    ])

if __name__ == '__main__':
    url = 'https://bbs.byr.cn/'
    #url = 'http://bbs.cloud.icybee.cn/default'
    #for i in range(1):
    ##    cur = request(url).read().decode('utf-8','ignore')
    #    print(cur)
    #    break
    app = make_app()
    server = HTTPServer(app)
    server.bind(port)
    server.start(16)  # Fork 多个子进程
    #app.listen(port)
    tornado.ioloop.IOLoop.current().start()
    IOLoop.current().start()
