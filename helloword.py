#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
	"""主路由处理类"""
	def get(self):
		# 对应的http的get请求方法
		self.write('Hello Itcast!')



if __name__ == '__main__':
	app = tornado.web.Application([(r'/',IndexHandler),])

	http_server = tornado.httpserver.HTTPServer(app)

	# app.listen(8000)

	http_server.bind(8000)
	# 注意这里吗如果start 后面是0 或则小于0  就默认开启处理器核心数的进程
	http_server.start(0)
	tornado.ioloop.IOLoop.current().start()
