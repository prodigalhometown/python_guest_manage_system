#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-28 03:24:05
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

from suds.client import Client

url = 'http://127.0.0.1:8000/?wsdl'
client = Client(url)
result = client.service.say_hello("bugmaster", 3)
print(result)
