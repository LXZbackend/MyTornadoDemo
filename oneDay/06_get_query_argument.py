#coding=utf-8
'''

	1.查询字符串 形如key1 = value& key2=value2
	2.请求体,(body)中发送的数据 比如表单数据 json xml
	3.提取url的特定部分,/blogs/2016/09/0001 可以在服务器的路由中用正则表达式截取
	4.在http报文的头部(header) 中增加自定义的字段,


'''
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import options,define
from tornado.web import RequestHandler,MissingArgumentError
define('port',default=8890,type=int,help='run server')

class IndexHandler(RequestHandler):
	def post(self):
		query_arg = self.get_query_argument('a')

		print query_arg


	def get(self):

		query_arg  = self.get_query_argument('a')
		query_args = self.get_query_arguments('a')
		print "这是传进来的数据",query_args
		# self.write("这是传进来的数据"+str(query_arg))
		self.write(str(query_args))




if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application([(r'/',IndexHandler)],debug=True)

	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()