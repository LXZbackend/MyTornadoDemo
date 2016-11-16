#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json

from tornado.web import RequestHandler,MissingArgumentError
from tornado.options import options,define

define('port',default='8888',type=int,help='set run port')
'''
	结论:
		这个文件主要是验证除了服务器返回的状态码,你也可以自己设置状态码,记住如果是标准的状态码,不需要设置 原因,他会默认以前的参数,
		但是,如果自己定义的状态码,需要写明reason如果不写 将会报错哦


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


		
		dic_dump = json.dumps(dic)
		# 这是标准的状态码 所以不用写原因
		# self.set_status(404)


		# 这是自定义的状态码,必须写明原因
		self.set_status(444,'lixianzhu')
		self.write(dic_dump)
		



if __name__ == '__main__':
	app = tornado.web.Application([
	(r'/',IndexHandler)                              





	],


	debug=True



								  )


	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)

	tornado.ioloop.IOLoop.current().start()
