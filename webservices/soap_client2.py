#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-28 01:26:21
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')

client = Client(url, plugins=[ImportDoctor(imp)])
result = client.service.getWeatherbyCityName('深圳')
print(result)