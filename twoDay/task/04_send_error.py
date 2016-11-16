# coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json

from tornado.web import RequestHandler, MissingArgumentError
from tornado.options import options, define

define('port', default='8888', type=int, help='set run port')
'''
	结论:这个文件主要是测试 send_error和write_error 配合使用的


	还有set_status 是设置状态码给浏览器看得,
	如果你想实现根据不同状态码 渲染同的页面怎么办?
	思路:你可以在get 中判断如果满足什么条件 就执行send_error,然后就会去执行
	write_error 你可以根据wirte_error 中传进来的状态码 渲染不同的页面.

	注意：使用send_error()方法后就不要再向输出缓冲区写内容了！

	bug 今天发生一个bug  就是在sublim 中已经看到对其了 但是用cat 或者vi 查看 还是对齐的
	




'''


class IndexHandler(RequestHandler):

    def set_default_headers(self):
        '''
                该方法会在进入HTTP处理方法前先被调用，可以重写此方法来预先设置默认的headers。注意：在HTTP处理方法中使用set_header()方法会覆盖掉在set_default_headers()方法中设置的同名header。

        '''
        # self.set_header("Content-Type",'Application/json;charset=UTF-8')
        self.set_header("itcast", "python")

    def write_error(self, status_code, **kwargs):
        print "这是write_error"
        self.write("报错了是404错误")

        if status_code == 404:
            self.write("报错了是404错误")
            self.write(kwargs['content'])

    def get(self):
        dic = {
            "name": 'liianzhu',
            'age': 12,
            'tel': 12312,
        }

        dic_dump = json.dumps(dic)
        self.write(dic_dump)
        # 当执行到这时候就会报错也不会写人任何数据,就是直接告诉服务器 出错了.
        print "这是send_error"
        self.send_error(404, content="出现404错误")
        # self.write(dic_dump)


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', IndexHandler)





    ],


        debug=True



    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()
