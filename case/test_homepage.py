# @Author ：黄贝尔
# @Time ：2020/12/4__15:01

import unittest
from selenium import webdriver
import time
from utils.seleniumtools import new_find_element
from utils.TUMIcn_login import login
from config import host,kefu_url,chromeDriver_Path
from PO.tumi_club import huiyuan_zhuanshuliyv
from PO.store_locator import mendianleixing
from PO.cart import empty_gouwuche
from PO.HOME_PAGE import lvxingxiang,huiyuanjulebu,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,gouwuche,denglu,jixv_gouwu

class test_homepage_nologin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=chromeDriver_Path)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        self.driver.get(f'{host}')
        self.driver.maximize_window()
        time.sleep(2)
    def test_TUMIUAT_408_1(self):
        assert new_find_element(self.driver,lvxingxiang).text == '旅行箱'
        assert new_find_element(self.driver,huiyuanjulebu).text == '会员俱乐部'
        assert new_find_element(self.driver,zhuce_denglu).text == '登录/注册'
    def test_TUMIUAT_408_2(self):
        new_find_element(self.driver, huiyuanjulebu).click()
        #self.driver.window_handles()#获取N个网页句柄
        self.driver.switch_to_window(self.driver.window_handles[-1])#切换到最新的网页
        assert self.driver.current_url == f'{host}/tumi-club/'
        assert new_find_element(self.driver,huiyuan_zhuanshuliyv).text == '会员专属礼遇'
    def test_TUMIUAT_408_3(self):
        new_find_element(self.driver,xianxiamendian).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{host}/store-locator/'
        assert new_find_element(self.driver,mendianleixing).text == '门店类型'
    def test_TUMIUAT_408_4(self):
        new_find_element(self.driver,zaixiankefu).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{kefu_url}'
        assert new_find_element(self.driver,tishi).text == '您正在和客服代表对话'
    def test_TUMIUAT_408_5(self):
        new_find_element(self.driver,gouwuche).click()
        assert self.driver.current_url ==f'{host}/cart'
        assert new_find_element(self.driver,empty_gouwuche).text == '您的购物车为空。'
    def test_TUMIUAT_408_6(self):
        new_find_element(self.driver,zhuce_denglu).click()
        time.sleep(2)
        assert new_find_element(self.driver,denglu).text == '登录'
