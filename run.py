# @Author ：黄贝尔
# @Time ：2020/12/4__15:01

import unittest
from utils.ClassicHTMLTestRunner import HTMLTestRunner
#自动收集测试用例
testcase = unittest.defaultTestLoader.discover('case','test_*.py')

#自动运行case并生成报告 htmltestrunner
filePath = r'D:\huang_Project\TUMI\report\report.html'
#D:\huang_Project\TUMI\report\report.html
#F:\Tuogo_Project\TUMI\report\report.html  家里
#C:\huang111\TUMI\report\report.html   公司
title = 'TUMI'
descr = 'TUMI'

with open(filePath,'wb') as f:
    runner =HTMLTestRunner(stream=f,title=title,description=descr)
    runner.run(testcase)