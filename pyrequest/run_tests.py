#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-24 00:56:54
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

# 指定测试用例为当前文件夹下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
	# 初始化接口测试数据
	test_data.init_data()

	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './report/' + now + '_result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp, title='Guest Manage System interface Test Report', description='Implementation Example with:')
	runner.run(discover)
	fp.close()
