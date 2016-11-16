# coding=utf-8
import tornado.web
import tornado.ioloop
# 新引入的httpserver模块
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):

	def get(self):
		self.write("lixianzhu")






if __name__ == '__main__':
    app = tornado.web.Application([(r'/', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    # z这是将服务器绑定在指定端口.
    http_server.bind(8080)
    # applisten(8888)http_server.listt
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()
