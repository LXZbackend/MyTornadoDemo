#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
from tornado.options import define,options
from tornado.web import url,RequestHandler

class IndexHandler(tornado.web.RequestHandler):

	def set_default_status(self):
		self.set_header("Content_Type","application/json;charset=utf-8")



	def get(self):
		stu  = {
		"name":"zhangsan",
		"age":24,
		"gender":1,
		}
		# 序列化
		stu_json = json.dumps(stu)
		self.set_header("Content_Type","application/json;charset=utf-8")
		self.write(stu_json)
		# self.set_status(444,'lixianzhu error')
		# self.write(stu)


class ItcastHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('hah')
		# self.redirect(self.reverse_url(myobject))
if __name__ == '__main__':
	app = tornado.web.Application([
	url(r'/',IndexHandler,name='myobject'),
	(r'/python',ItcastHandler),
	],defbug=True)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8888)


	tornado.ioloop.IOLoop.current().start()