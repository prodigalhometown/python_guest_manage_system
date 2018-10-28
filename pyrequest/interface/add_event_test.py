#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-24 00:25:29
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

import unittest
import requests
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
	'''添加发布会'''

	def setUp(self):
		self.base_url = "http://127.0.0.1:8000/api/add_event/"

	def tearDown(self):
		print(self.result)

	def test_add_event_all_null(self):
		'''all the parameter are null'''
		payload = {'eid': '', 'name': '', 'limit': '', 'address': '', 'start_time': '', 'create_time': ''}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 10021)
		self.assertEqual(self.result['message'], 'parameter error')

	def test_add_event_eid_exist(self):
		"""eid is exist"""
		payload = {'eid': '1', 'name': '一加4发布会', 'limit': '2000', 'address': '深圳宝体', 'start_time': '2018', 'create_time': '2018-10-29 14:00:00'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 10022)
		self.assertEqual(self.result['message'], 'event id is already exists')

	def test_add_event_name_exist(self):
		"""name is exist"""
		payload = {'eid': '11', 'name': '红米Pro发布会', 'limit': '2000', 'address': '深圳宝体', 'start_time': '2018', 'create_time': '2018-10-29 14:00:00'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 10023)
		self.assertEqual(self.result['message'], 'event name is already exists')

	def test_add_event_date_type_error(self):
		"""date type error"""
		payload = {'eid': '11', 'name': '一加4手机发布会', 'limit': '2000', 'address': '深圳宝体', 'start_time': '2018', 'create_time': '2018-10-29 14:00:00'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 10024)
		self.assertIn('start_time format error.', self.result['message'])

	def test_add_event_success(self):
		"""add success"""
		payload = {'eid': '11', 'name': '一加4手机发布会', 'limit': '2000', 'address': '深圳宝体', 'start_time': '2018-10-29 14:00:00', 'create_time': '2018-10-29 14:00:00'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 200)
		self.assertEqual(self.result['message'], 'add event success')

if __name__ == '__main__':
	# init interface test datas
	test_data.init_data()
	# execute testcase
	unittest.main()