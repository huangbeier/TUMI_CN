# @Author ：黄贝尔
# @Time ：2021/2/7__11:03
# #coding:utf-8
import unittest
from test_po import search
from selenium import webdriver
import time

class testsearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(r'C:\Users\huang\Desktop\chromedriver.exe')
    def setUp(self):
        url = 'https://www.baidu.com/'
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)
    def test_001(self):
        driver=self.driver
        text='搜索'
        search_page = search(driver)
        search_page.input_search_text(text)
        search_page.click_button()

    def tearDownClass(cls):
        cls.driver.quit()

