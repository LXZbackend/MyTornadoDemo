#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
from tornado.options import define,options

class IndexHandler(tornado.web.RequestHandler):
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
		# self.write(stu)


if __name__ == '__main__':
	app = tornado.web.Application([(r'/',IndexHandler)],defbug=True)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8888)


	tornado.ioloop.IOLoop.current().start()