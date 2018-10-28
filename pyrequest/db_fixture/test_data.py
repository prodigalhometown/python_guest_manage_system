#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-24 00:00:45
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

import sys
sys.path.append('../db_fixture')
from mysql_db import DB

# 创建测试数据
datas = {
	# 发布会表数据
	'sign_event': [
		{'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': '2018-10-29 14:00:00', 'create_time': '2018-10-29 14:00:00'},
		{'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '北京会展中心', 'start_time': '2018-10-29 14:00:00', 'create_time': '2018-10-29 14:00:00'},
		{'id': 3, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0, 'address': '北京会展中心', 'start_time': '2018-10-29 14:00:00', 'create_time': '2018-10-29 14:00:00'},
		{'id': 4, 'name': '发布会已结束', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': '2017-10-29 14:00:00', 'create_time': '2018-10-29 14:00:00'},
		{'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': '2018-10-29 14:00:00', 'create_time': '2018-10-29 14:00:00'},
	],
	# 嘉宾表数据
	'sign_guest': [
		{'id': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mial.com', 'sign': 0, 'create_time': '2018-10-29 14:00:00', 'event_id': 1},
		{'id': 2, 'realname': 'has sign', 'phone': 13511001101, 'email': 'sign@mial.com', 'sign': 1, 'create_time': '2018-10-29 14:00:00', 'event_id': 1},
		{'id': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mial.com', 'sign': 0, 'create_time': '2018-10-29 14:00:00', 'event_id': 5},
	],
}

# 将测试数据插入表
def init_data():
	db = DB()
	for table, data in datas.items():
		db.clear(table)
		for d in data:
			db.insert(table, d)
	db.close()

if __name__ == '__main__':
	init_data()