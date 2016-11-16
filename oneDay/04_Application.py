# coding=utf-8
import tornado.web
import tornado.ioloop
# 新引入的httpserver模块
import tornado.httpserver
import tornado.options

'''
	文件是在路由银色表中传入参数
'''
# 自己定义传入的参数名称.

tornado.options.define('port',default=8080,type=int,help='设置端口')
# 这是传入一个参数.


class IndexHandler(tornado.web.RequestHandler):

	def get(self):
		print"asdfas"
		self.write("lixianzhu")


class ItcastHandler(tornado.web.RequestHandler):

	def get(self):
		
		self.write(self.subject)

	def initialize(self,subject):
		self.subject = subject
		




if __name__ == '__main__':
	tornado.options.parse_command_line()

	app = tornado.web.Application([
	 (r'/', IndexHandler),
	 (r'/cpp',ItcastHandler,{"subject":"c++"}),
	 (r'/python',ItcastHandler,{"subject":"python"})
	 ])
	
	http_server = tornado.httpserver.HTTPServer(app)

	# z这是将服务器绑定在指定端口.
	http_server.bind(tornado.options.options.port)
	# applisten(8888)http_server.listt
	print tornado.options.options.port
	http_server.start(0)
	tornado.ioloop.IOLoop.current().start()
