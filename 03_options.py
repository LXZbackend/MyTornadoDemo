#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define('port',type=int,default=8000,help='服务器端口')

class IndexHandler(tornado.web.RequestHandler):
	"""主路由处理类"""
	def get(self):
		# 对应的http的get请求方法
		self.write('Hello Itcast!')



if __name__ == '__main__':

	tornado.options.parse_command_line()
	print 'port',tornado.options.options.port

	app = tornado.web.Application([(r'/',IndexHandler)])

	http_server = tornado.httpserver.HTTPServer(app)
	# app.listen(8000)
	http_server.bind(tornado.options.options.port)
	# 注意这里吗如果start 后面是0 或则小于0  就默认开启处理器核心数的进程
	tornado.ioloop.IOLoop.current().start()
