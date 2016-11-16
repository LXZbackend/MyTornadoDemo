# coding=utf-8
import tornado.web
import tornado.ioloop
# 新引入的httpserver模块
import tornado.httpserver
import tornado.options
import os

# 自己定义传入的参数名称.

tornado.options.define('port',default=8080,type=int,help='设置端口')
# 这是传入一个参数.

class IndexHandler(tornado.web.RequestHandler):

	def get(self):
		print"asdfas"
		self.write("lixianzhu")






if __name__ == '__main__':
	tornado.options.parse_command_line()
	current_path = os.path.dirname(__file__)
	app = tornado.web.Application([
	(r'/itcast', IndexHandler),
	(r'/(.*)',StaticFileHandler,{'path':os.path.join(current_path,'statics/html'),"default_filename":'index.html'})




	],


	static_path = os.path.join(current_path,'static'),
	templata_path = os.path.join(current_path,'templates'),
	debug = True

	)











	http_server = tornado.httpserver.HTTPServer(app)
	# z这是将服务器绑定在指定端口.
	http_server.bind(tornado.options.options.port)
	# applisten(8888)http_server.listt
	print tornado.options.options.port
	http_server.start(0)
	tornado.ioloop.IOLoop.current().start()
