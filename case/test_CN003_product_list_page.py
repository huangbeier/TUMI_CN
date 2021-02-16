# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-02-15
import unittest
import time
from selenium import webdriver
from config import chromeDriver_Path,cn_url
from utils.seleniumtools import new_find_element
from CN_001_homepage import homepage
from CN_003_product_list_page import product_list
from config import cn_url

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
    # def tearDown(self):
    #     homepage1 = homepage(self.driver)
    #     my_account1 = my_account(self.driver)
    #     time.sleep(2)
    #     my_account1.move_to_logo()
    #     my_account1.click_account_logo()
    #     if new_find_element(self.driver,homepage.my_username).text != '登录/注册':
    #         homepage1.sign_out()

    def test_058_TUMIUAT_449_1(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_f_homepage()
        assert self.driver.current_url == cn_url

    def test_059_TUMIUAT_449_2(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_backpack()
        product_list1.click_f_homepage()
        assert self.driver.current_url == cn_url

    def test_060_TUMIUAT_449_3(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_bag()
        product_list1.click_f_homepage()
        assert self.driver.current_url == cn_url

    def test_061_TUMIUAT_449_4(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_accessories()
        product_list1.click_f_homepage()
        assert self.driver.current_url == cn_url

    def test_062_TUMIUAT_449_5(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_diy()
        product_list1.click_f_homepage()
        assert self.driver.current_url == cn_url

    def test_063_TUMIUAT_450_1(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_all_product()
        assert new_find_element(self.driver,homepage.luggage_title).text  == '各类旅行箱 - 托运旅行箱、登机箱'

    def test_064_TUMIUAT_450_2(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_backpack()
        product_list1.click_all_product()
        assert new_find_element(self.driver,homepage.backpacks_title).text  == '各类背包 - 商务、旅行、休闲背包'

    def test_065_TUMIUAT_450_3(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_bag()
        product_list1.click_all_product()
        assert new_find_element(self.driver,homepage.bag_title).text  == '各类手袋 - 手拎包、斜挎包、公文包'

    def test_066_TUMIUAT_450_4(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_accessories()
        product_list1.click_all_product()
        assert new_find_element(self.driver,homepage.accessories_title).text  == '各类旅行配件、电子产品、钱包等'

    def test_067_TUMIUAT_451(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        assert new_find_element(self.driver,product_list.s_luggage_title).text == '登机箱 - 旅行拉杆箱'

    def test_068_TUMIUAT_452(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_homepage()
        assert self.driver.current_url == cn_url

    def test_069_TUMIUAT_453_1(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_compare()
        assert new_find_element(self.driver,product_list.compare_text).text == '添加1或2个商品'

    def test_070_TUMIUAT_453_2(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_compare()
        product_list1.click_s_compare()
        assert new_find_element(self.driver,product_list.immediately_to_compare).text == '立即比较'

    def test_071_TUMIUAT_453_3(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_compare()
        product_list1.click_s_compare()
        product_list1.click_t_compare()
        product_list1.click_fo_compare()
        assert new_find_element(self.driver,product_list.compare_error).text == '您一次最多可以比较3个产品'

    def test_072_TUMIUAT_454(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        time.sleep(3)
        assert new_find_element(self.driver,product_list.hide_the_screening).text == '隐藏筛选'
        assert new_find_element(self.driver, product_list.screening_series).text == '系列'
        assert new_find_element(self.driver, product_list.screening_color).text == '颜色组'
        assert new_find_element(self.driver, product_list.screening_prices).text == '价格'
        assert new_find_element(self.driver, product_list.screening_material).text == '材料'
        assert new_find_element(self.driver, product_list.screening_sex).text == '性别'
        assert new_find_element(self.driver, product_list.screening_function).text == '专属功能'
        assert new_find_element(self.driver, product_list.screening_size).text == '电脑尺寸'
        assert new_find_element(self.driver, product_list.screening_type).text == '产品类型'
        assert new_find_element(self.driver, product_list.screening_luggage_size).text == '行李箱尺寸'
        assert new_find_element(self.driver, product_list.screening_roller).text == '滚轮数量'