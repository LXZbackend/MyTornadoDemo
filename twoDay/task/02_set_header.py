#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json

from tornado.web import RequestHandler,MissingArgumentError
from tornado.options import options,define

define('port',default='8888',type=int,help='set run port')
'''
	这个验证了 自己可以设置Response-header ("Content-Type",'Application/json;charset=UTF-8')
	2.除了你可以设置默认的头部信息,你可以自己定义新的头部字段.头部信息都是类字典的你可以通过添加自己新的键,你也可以在get方法中覆盖 或者自己在添加新的头部信息


'''
class IndexHandler(RequestHandler):
	def set_default_headers(self):
		'''
			该方法会在进入HTTP处理方法前先被调用，可以重写此方法来预先设置默认的headers。注意：在HTTP处理方法中使用set_header()方法会覆盖掉在set_default_headers()方法中设置的同名header。

		'''
		# self.set_header("Content-Type",'Application/json;charset=UTF-8')
		self.set_header("itcast", "python")







	def get(self):
		dic = {
		"name":'liianzhu',
		'age':12,
		'tel':12312,
		}


		print type(dic)
		dic_dump = json.dumps(dic)
		print type(dic_dump)

		self.write(dic_dump)
		# self.set_header("Content-Type",'Application/json;charset=UTF-8')
		# 这是在http中添加新的头部信息
		self.set_header("lixianzhu", "i love python")
		# 这是修改上头默认的头部信息,如果没又就建立新的字典
		self.set_header("itcast", "i love python")



if __name__ == '__main__':
	app = tornado.web.Application([
	(r'/',IndexHandler)                              





	],


	debug=True



								  )


	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)

	tornado.ioloop.IOLoop.current().start()
