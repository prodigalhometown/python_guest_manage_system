#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-28 00:05:22
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

from suds.client import Client

# 使用库suds_jurko: https://bitbucket.org/jurko/suds
# Web Services 查询: http://www.webxml.com.cn/zh_cn/web_services.aspx

# 电话号码归属地查询
url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
# print(client)
result = client.service.getMobileCodeInfo('18665377693')
print(result)