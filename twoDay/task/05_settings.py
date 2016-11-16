#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json
import os

from tornado.web import RequestHandler,MissingArgumentError,url,StaticFileHandler
from tornado.options import options,define

define('port',default='8888',type=int,help='set run port')
'''

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
	current_path = os.path.dirname(__file__)
	app = tornado.web.Application([
	# (r'/',IndexHandler),
	(r'/(.*)',StaticFileHandler,{'path':os.path.join(current_path,'static/html'),"default_filename":"index.html"}),                             





	],

	start_path = os.path.join(current_path,'static'),
	template_path=os.path.join(current_path, "templates"),
	debug=True,



								  )


	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()
