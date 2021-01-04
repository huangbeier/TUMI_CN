# @Author ：黄贝尔
# @Time ：2021/1/4__11:02
# #coding:utf-8
import unittest
from selenium import webdriver
import time
from utils.seleniumtools import new_find_element
from config import host,kefu_url,chromeDriver_Path
from PO.tumi_club import huiyuan_zhuanshuliyv
from PO.store_locator import mendianleixing
from PO.HOME_PAGE import lvxingxiang,huiyuanjulebu,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,gouwuche,denglu,jixv_gouwu,username,password,close_login,my_account1,sousuo,sousuo_anniu,\
    guanjianzi
from PO.my_account import my_account

class test_homepage_login(unittest.TestCase):
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
        # flag=self.driver.find_elements_by_link_text('登录/注册')
        # if len(flag)==1:
        #     new_find_element(self.driver, zhuce_denglu).click()
        #     time.sleep(1)
        #     new_find_element(self.driver, username).send_keys('17316565325')
        #     new_find_element(self.driver, password).send_keys('gxjy541')
        #     time.sleep(2)
        #     new_find_element(self.driver, denglu).click()
        #     time.sleep(2)
        #     new_find_element(self.driver,close_login).click()
        #     self.driver.refresh()#登陆完后刷新页面
        #     time.sleep(1)
        # else:
        #     pass
    def tearDown(self):
        self.driver.close()
    def test_TUMIUAT_409_1(self):
        assert new_find_element(self.driver, lvxingxiang).text == '旅行箱'
        assert new_find_element(self.driver, huiyuanjulebu).text == '会员俱乐部'
    def test_TUMIUAT_409_2(self):
        new_find_element(self.driver, huiyuanjulebu).click()
        # self.driver.window_handles()#获取N个网页句柄
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{host}/tumi-club/'
        assert new_find_element(self.driver, huiyuan_zhuanshuliyv).text == '会员专属礼遇'
    def test_TUMIUAT_409_3(self):

        new_find_element(self.driver, xianxiamendian).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{host}/store-locator/'
        assert new_find_element(self.driver, mendianleixing).text == '门店类型'
    def test_TUMIUAT_409_4(self):
        new_find_element(self.driver, zaixiankefu).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{kefu_url}'
        assert new_find_element(self.driver, tishi).text == '您正在和客服代表对话'
    def test_TUMIUAT_409_5(self):
        new_find_element(self.driver, gouwuche).click()
        time.sleep(1)
        assert new_find_element(self.driver, jixv_gouwu).text == '继续购物'
    def test_TUMIUAT_409_6(self):
        new_find_element(self.driver,my_account1).click()
        time.sleep(2)
        assert new_find_element(self.driver, my_account).text == '我的账号'
    def test_TUMIUAT_410_1(self):
        new_find_element(self.driver,sousuo).send_keys('alp')
        new_find_element(self.driver,sousuo_anniu).click()
        assert self.driver.find_element_by_xpath('//*[@id="productTabContent"]/div[1]/div/div[1]/h1').text == '搜索页'
    def test_TUMIUAT_410_2(self):
        new_find_element(self.driver, sousuo).send_keys('alp')
        time.sleep(10)
        assert new_find_element(self.driver,guanjianzi).text == '建议关键字'