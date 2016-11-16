# coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options
from tornado.web import RequestHandler, url


class IndexHandler(RequestHandler):

	def get(self):

		# query_arg = self.get_query_argument('q')
		query_argas = self.get_query_arguments('q')

		self.write(str(query_argas))



if __name__ == '__main__':
	app=tornado.web.Application(
		[(r'/', IndexHandler)
		], debug=True)


	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
