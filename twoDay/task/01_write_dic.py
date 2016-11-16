#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json

from tornado.web import RequestHandler,MissingArgumentError
from tornado.options import options,define

define('port',default='8888',type=int,help='set run port')
'''
	验证了:当你往页面传字典的格式时,当你没有序列化传过去,这时候response header
	Content-Type:application/json; charset=UTF-8
	当你序列化穿过去后 就会变成,Content-Type:text/html; charset=UTF-8

'''
class IndexHandler(RequestHandler):
	def get(self):
		dic = {
		"name":'liianzhu',
		'age':12,
		'tel':123123123123,
		}


		print type(dic)
		dic_dump = json.dumps(dic)
		print type(dic_dump)

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
