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



	def write_error(self,scode,**kwargs):
		self.write('出错了<br/>')
		self.write("标题%s<br/>"%kwargs.get('err_title',''))
		self.write("详情%s<br/>"%kwargs.get('err_content',''))
		self.write(kwargs.get('err_content',''))




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

		# self.send_error(404,err_content='lixainzhu',err_title='haha')

		# self.set_status(444,'lixianzhu error')
		# self.write(stu)

if __name__ == '__main__':
	app = tornado.web.Application([
	url(r'/',IndexHandler,name='myobject')])
	
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8888)


	tornado.ioloop.IOLoop.current().start()