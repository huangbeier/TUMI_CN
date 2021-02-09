# @Author ：黄贝尔
# @Time ：2021/2/9__13:39
# #coding:utf-8
import unittest
from CN_002_My_Account import my_account
from CN_other import my_account_assert_element
import time
from selenium import webdriver
from config import chromeDriver_Path,cn_kefu_url,cn_url,cn_cart,cn_account
from utils.seleniumtools import new_find_element
from CN_001_homepage import homepage

class MyAccount(unittest.TestCase):
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

    def tearDown(self):
        homepage1 = homepage(self.driver)
        my_account1 = my_account(self.driver)
        time.sleep(2)
        my_account1.move_to_logo()
        my_account1.click_account_logo()
        if new_find_element(self.driver,homepage.my_username).text != '登录/注册':
            homepage1.sign_out()

    def test_032_TUMIUAT_564(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_info()
        assert new_find_element(self.driver,my_account_assert_element.my_account_title).text == '个人信息'

    def test_033_TUMIUAT_565(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        assert new_find_element(self.driver,my_account.update_my_info).text == '更新个人信息'
        assert new_find_element(self.driver,my_account.update_my_password).text == '更新密码'
        assert new_find_element(self.driver,my_account.my_address).text == '我的地址簿'

    def test_034_TUMIUAT_1529_1(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        time.sleep(6)
        b=new_find_element(self.driver,my_account.nearby_stores).text
        my_account1.click_nearby_stores()
        a = new_find_element(self.driver,my_account_assert_element.store_name).text
        assert b == a

    def test_035_TUMIUAT_1529_2(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        time.sleep(6)
        my_account1.click_nearby_stores()
        my_account1.click_store_search()
        assert new_find_element(self.driver,my_account_assert_element.store_type).text == '门店类型'

    def test_036_TUMIUAT_566(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.input_diy()
        time.sleep(1)
        my_account1.click_diy_btn()
        time.sleep(1)
        assert new_find_element(self.driver, my_account_assert_element.diy_title).text == '点击下方输入框激活个性化定制，激活后在输入框内输入您想要定制的字母'
        self.driver.refresh()

    def test_037_TUMIUAT_567(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_info()
        my_account1.clear_account_username()
        my_account1.input_account_username()
        my_account1.click_account_call()
        my_account1.click_call_miss()
        my_account1.clear_account_email()
        my_account1.input_account_email()
        my_account1.click_account_save_btn()
        assert new_find_element(self.driver, my_account_assert_element.update_my_info).text == '更新个人信息'




