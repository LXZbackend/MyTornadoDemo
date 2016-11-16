#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define,options
from tornado.web import RequestHandler,url



class IndexHandler(RequestHandler):
	def get(self):
		mystring = '<a href=""></a>'

		self.write()


class SubjectHandler(RequestHandler):
	def initialize(self,subject):
		self.subject = subject
	def get(self):
		self.write(self.subject)


if __name__=='__main__':
	app = tornado.web.Application(
		[(r'/',IndexHandler), 
	    (r'/python',SubjectHandler,{'subject':'python'}),
	    url(r'/cpp',SubjectHandler,{'subject':'cpp'},name='cpp_url'),


	    ],debug = True)


	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()