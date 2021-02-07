# @Author ：黄贝尔
# @Time ：2021/2/7__11:03
# #coding:utf-8
from utils.seleniumtools import new_find_element
class page(object):
    def __int__(self,driver):
        self.driver=driver
        # self.url=url
        self.timeout=30

    def input_text(self,loc,text):
        new_find_element(self.driver,loc).send_keys(text)

    def click(self,loc):
        new_find_element(self.driver,loc).click()

