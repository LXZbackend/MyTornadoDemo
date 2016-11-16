# coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options
from tornado.web import RequestHandler, url
import json


class IndexHandler(RequestHandler):

	def post(self):

		# query_arg = self.get_query_argument('q')
		# query_argas = self.get_query_arguments('q')
	 	# flag = self.request.headers.get("Content-Type").startswith('applicaion/json')
	 	# if flag:
 		json_data = self.request.body
 		print json_data
 		print type(json_data)

 		json_data = json.loads(json_data)
 		print json_data
 		print type(json_data)
 		# img = self.request.files['img1'][0]['body']

 		# f = open('1.jpg','a')

 		# f.write(img)
 		# f.close()



 		# print img



		self.write("ok")



if __name__ == '__main__':
	app=tornado.web.Application(
		[(r'/', IndexHandler)
		], debug=True)


	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
