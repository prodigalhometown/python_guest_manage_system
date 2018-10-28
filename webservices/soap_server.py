#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-28 02:44:03
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11

class HelloWorldService(ServiceBase):
	@rpc(Unicode, Integer, _returns=Iterable(Unicode))
	def say_hello(ctx, name, times):
		for i in range(times):
			yield 'Hello, %s' % name

application = Application([HelloWorldService],
	tns='spyne.examples.hello',
	in_protocol=Soap11(validator='lxml'),
	out_protocol=Soap11()
)

if __name__ == '__main__':
	# You can use any Wsgi server. Here, we chose
	# Python's built-in wsgi server but you're not supposed to use it in production
	from wsgiref.simple_server import make_server
	wsgi_app = WsgiApplication(application)
	server = make_server('127.0.0.1', 8000, wsgi_app)
	server.serve_forever()
