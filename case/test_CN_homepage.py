# @Author ：黄贝尔
# @Time ：2021/2/7__13:37
# #coding:utf-8
import unittest
from CN_homepage import homepage
from CN_other import assert_element
import time
from selenium import webdriver
from selenium.webdriver import ActionChains  #实现鼠标悬停
from config import chromeDriver_Path,cn_kefu_url,cn_url,cn_cart,cn_account
from utils.seleniumtools import new_find_element

class HOMEPAGE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(chromeDriver_Path)
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    def setUp(self):
        self.driver.get(cn_url)
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(2)

    def test_TUMIUAT_408_1(self):
        homepage1 = homepage(self.driver)
        homepage1.click_logo()
        assert self.driver.current_url == cn_url

    def test_TUMIUAT_408_2(self):
        homepage1 = homepage(self.driver)
        homepage1.click_vip_club()
        assert self.driver.current_url == 'https://www.tumi.cn/tumi-club/'
        assert new_find_element(self.driver,assert_element.vip_Privilege).text == '会员专属礼遇'

    def test_TUMIUAT_408_3(self):
        homepage1 = homepage(self.driver)
        homepage1.move_to_wechat()
        # assert new_find_element(self.driver,assert_element.wechat_text).text == '扫一扫进入TUMI途明 微信精品店'

    def test_TUMIUAT_408_4(self):
        homepage1 = homepage(self.driver)
        homepage1.click_offline_store()
        assert self.driver.current_url == 'https://www.tumi.cn/store-locator/'
        assert new_find_element(self.driver,assert_element.store_type).text == '门店类型'

    def test_TUMIUAT_408_5(self):
        homepage1 = homepage(self.driver)
        homepage1.click_customer_service()
        assert self.driver.current_url == cn_kefu_url

    def test_TUMIUAT_408_6(self):
        homepage1 = homepage(self.driver)
        homepage1.click_cart()
        assert self.driver.current_url == cn_cart

    def test_TUMIUAT_408_7(self):
        homepage1 = homepage(self.driver)
        homepage1.click_login()
        # a=assert_element.login_text.text
        # print(a)
        time.sleep(0.5)
        assert new_find_element(self.driver,assert_element.login_text).text == '登录您的TUMI.CN账号'

    def test_TUMIUAT_409_1(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_logo()
        assert self.driver.current_url == cn_url

    def test_TUMIUAT_409_2(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_vip_club()
        assert self.driver.current_url == 'https://www.tumi.cn/tumi-club/'
        assert new_find_element(self.driver,assert_element.vip_Privilege).text == '会员专属礼遇'

    def test_TUMIUAT_409_3(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.move_to_wechat()
        # assert new_find_element(self.driver,assert_element.wechat_text).text == '扫一扫进入TUMI途明 微信精品店'

    def test_TUMIUAT_409_4(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_offline_store()
        assert self.driver.current_url == 'https://www.tumi.cn/store-locator/'
        assert new_find_element(self.driver,assert_element.store_type).text == '门店类型'

    def test_TUMIUAT_409_5(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_customer_service()
        assert self.driver.current_url == cn_kefu_url

    def test_TUMIUAT_409_6(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_cart()
        assert self.driver.current_url == cn_cart

    def test_TUMIUAT_409_7(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_my_username()
        assert self.driver.current_url == cn_account

    def test_TUMIUAT_410(self):
        homepage1 = homepage(self.driver)
        homepage1.search_for_Effective_Products()
        time.sleep(1)
        assert new_find_element(self.driver,homepage.keyword).text == '建议关键字 "alpha"'

    def test_TUMIUAT_411(self):
        homepage1 = homepage(self.driver)
        homepage1.Search_for_Invalid_Products()
        assert new_find_element(self.driver,assert_element.no_search).text == '对不起，没有搜索结果'

    def test_TUMIUAT_412(self):
        homepage1 = homepage(self.driver)
        homepage1.search_for_Effective_Products()
        homepage1.click_suggested_keyword()
        assert new_find_element(self.driver, assert_element.have_search).text == '搜索结果'

    def test_TUMIUAT_1510_1(self):
        homepage1 = homepage(self.driver)
        homepage1.click_f_luggage()
        print(self.driver.current_url)
        assert self.driver.current_url == f'{cn_url}c-luggage/'
        assert new_find_element(self.driver, assert_element.luggage_title).text =='各类旅行箱 - 托运旅行箱、登机箱'

    def test_TUMIUAT_1510_2(self):
        homepage1 = homepage(self.driver)
        homepage1.click_f_backpacks()
        print(self.driver.current_url)
        assert self.driver.current_url == f'{cn_url}c-backpacks/'
        assert new_find_element(self.driver, assert_element.backpacks_title).text =='各类背包 - 商务、旅行、休闲背包'









