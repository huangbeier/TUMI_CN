# @Author ：黄贝尔
# @Time ：2021/2/18__10:40
# #coding:utf-8
import unittest
import time
from selenium import webdriver
from config import chromeDriver_Path,cn_url
from utils.seleniumtools import new_find_element
from CN_003_product_list_page import product_list
from config import cn_url
from CN_004_product_details_page import product_details_page
from CN_001_homepage import homepage

class Product_list(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(chromeDriver_Path)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        self.driver.get(cn_url)
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(2)

    def test_087_TUMIUAT_479_1(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_product_img()
        product_list1.click_f_homepage()
        assert self.driver.current_url == cn_url

    def test_088_TUMIUAT_479_2(self):
        product_details_page1 = product_details_page(self.driver)
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_product_img()
        product_details_page1.click_f_crumbs()
        assert new_find_element(self.driver,homepage.luggage_title).text == '各类旅行箱 - 托运旅行箱、登机箱'

    def test_089_TUMIUAT_479_3(self):
        product_details_page1 = product_details_page(self.driver)
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_product_img()
        product_details_page1.click_s_crumbs()
        assert new_find_element(self.driver,product_details_page.s_type_title).text == '登机箱 - 旅行拉杆箱'

    def test_090_TUMIUAT_490(self):
        product_details_page1 = product_details_page(self.driver)
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_product_img()
        product_details_page1.click_share_blog()
        assert self.driver.title == '分享到微博-微博-随时随地分享身边的新鲜事儿'

    def test_091_TUMIUAT_491(self):
        product_details_page1 = product_details_page(self.driver)
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_product_img()
        product_details_page1.action_share_wechat()
        time.sleep(2)
        assert new_find_element(self.driver,product_details_page.wechat_text).text == '微信扫一扫'

