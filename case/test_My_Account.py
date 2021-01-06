# @Author ：黄贝尔
# @Time ：2021/1/6__10:26
# #coding:utf-8
import unittest
from selenium import webdriver
import time
from utils.seleniumtools import new_find_element
from config import host,kefu_url,chromeDriver_Path
from PO.tumi_club import huiyuan_zhuanshuliyv
from PO.store_locator import mendianleixing
from PO.HOME_PAGE import lvxingxiang,huiyuanjulebu,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,gouwuche,denglu,jixv_gouwu,username,password,close_login,gerenxinxi
from PO.my_account import mb_gerenxinxi,mb_dizhibu,mb_gengxinmima,mb_gengxingerenxinxi,geren_username,\
    geren_baocun,geren_chenghu,geren_qingxuanze
from selenium.webdriver import ActionChains


class test_My_Account(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = webdriver.ChromeOptions()
        driver.add_argument('disable-infobars')
        driver.add_argument('headless')  # 以后台运行
        cls.driver = webdriver.Chrome(executable_path=chromeDriver_Path)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        self.driver.get(f'{host}')
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(5)
        flag = self.driver.find_elements_by_link_text('登录/注册')
        if len(flag) == 1:
            new_find_element(self.driver, zhuce_denglu).click()
            time.sleep(1)
            new_find_element(self.driver, username).send_keys('17316565325')
            new_find_element(self.driver, password).send_keys('gxjy541')
            time.sleep(2)
            new_find_element(self.driver, denglu).click()
            time.sleep(2)
            new_find_element(self.driver, gerenxinxi).click()
            # new_find_element(self.driver, close_login).click()
            # self.driver.refresh()  # 登陆完后刷新页面
            # time.sleep(1)
        else:
            pass
    def test_TUMIUAT_564_565(self):
        time.sleep(1)
        assert new_find_element(self.driver,mb_gerenxinxi).text == '个人信息'
        assert self.driver.current_url == f'{host}/my-account/profile'
        assert new_find_element(self.driver,mb_dizhibu).text == '我的地址簿'
        assert new_find_element(self.driver, mb_gengxinmima).text == '更新密码'
        assert new_find_element(self.driver, mb_gengxingerenxinxi).text == '更新个人信息'
    def test_TUMIUAT_568(self):
        new_find_element(self.driver,mb_gengxingerenxinxi).click()
        new_find_element(self.driver,geren_username).clear()
        new_find_element(self.driver,geren_baocun).click()
        time.sleep(2)
        assert self.driver.find_element_by_id('userName.errors').text == '请输入用户名'
    def test_TUMIUAT_1578(self):
        new_find_element(self.driver,mb_gengxingerenxinxi).click()
        new_find_element(self.driver,geren_chenghu).click()
        new_find_element(self.driver, geren_qingxuanze).click()
        new_find_element(self.driver, geren_baocun).click()
        time.sleep(2)
        assert self.driver.find_element_by_id('titleCode.errors').text == '请选择您的称呼'
    def test_TUMIUAT_1579(self):
        new_find_element(self.driver,mb_gengxingerenxinxi).click()
        new_find_element(self.driver,geren_chenghu).click()
        self.driver.find_element_by_css_selector('#profile\.titleSelectBoxItOptions > li.selectboxit-option.selectboxit-focus > a').click()
        new_find_element(self.driver, geren_baocun).click()
        time.sleep(2)
        assert new_find_element(self.driver, mb_gengxingerenxinxi).text == '更新个人信息'



