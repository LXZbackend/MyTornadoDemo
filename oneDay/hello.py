#coding=utf-8
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hello word")




if __name__ == '__main__':
	app = tornado.web.Application([(r'/',IndexHandler)],debug = True)

	app.listen(8000)
	tornado.ioloop.IOLoop.current().start()	