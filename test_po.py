# @Author ：黄贝尔
# @Time ：2021/2/7__11:03
# #coding:utf-8
from test_base import page

class search(page):
    #搜索框
    search_input=('id','kw')
    #搜索按钮
    search_button=('id','su')
    def __init__(self,driver):
        page.__int__(self, driver)

    def input_search_text(self,text):
        self.input_text(self.search_input,text)

    def click_button(self):
        self.click(self.search_button)



