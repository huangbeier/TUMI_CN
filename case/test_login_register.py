# @Author ：黄贝尔
# @Time ：2021/1/5__16:59
# #coding:utf-8
import unittest
from selenium import webdriver
import time
from utils.seleniumtools import new_find_element
from config import host,kefu_url,chromeDriver_Path
from PO.tumi_club import huiyuan_zhuanshuliyv
from PO.store_locator import mendianleixing
from PO.cart import empty_gouwuche
from PO.HOME_PAGE import lvxingxiang,huiyuanjulebu,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,gouwuche,sousuo,sousuo_anniu,fenlei_lvxingxiang,fenlei_beibao,fenlei_tuotebao,fenlei_xiekuabao,\
    fenlei_peijian,fenlei_recycled,password,denglu,username
from selenium.webdriver import ActionChains  #实现鼠标悬停

class test_login_register(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('headless')  # 以后台运行
        cls.driver=webdriver.Chrome(executable_path=chromeDriver_Path)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        self.driver.get(f'{host}')
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(15)# 设定页面加载限制时间
        self.driver.execute_script('window.stop()')# 超时报错后就强制停止加载
        self.driver.refresh()
        time.sleep(3)
    def test_TUMIUAT_1514(self):
        # ActionChains(self.driver).move_to_element(new_find_element(self.driver,zhuce_denglu)).perform()  # 鼠标悬停到搜索框
        # time.sleep(5)
        new_find_element(self.driver,zhuce_denglu).click()
        time.sleep(1)
        new_find_element(self.driver,password).send_keys('gxjy541')
        time.sleep(2)
        new_find_element(self.driver, denglu).click()
        assert self.driver.find_element_by_id('j_username-error').text == '手机/邮箱 为必填选项'
    def test_TUMIUAT_1515(self):
        new_find_element(self.driver,zhuce_denglu).click()
        time.sleep(1)
        new_find_element(self.driver, username).send_keys('17316565324')
        new_find_element(self.driver,password).send_keys('gxjy541')
        new_find_element(self.driver, denglu).click()
        time.sleep(2)
        assert self.driver.find_element_by_css_selector('#tm-login-form > div.form_error-message-container.active > div').text == '你的用户名或密码不正确。'
    def test_TUMIUAT_423(self):
        new_find_element(self.driver,zhuce_denglu).click()
        time.sleep(1)
        new_find_element(self.driver, username).send_keys('17316565325')
        new_find_element(self.driver, denglu).click()
        time.sleep(2)
        assert self.driver.find_element_by_css_selector('#tm-login-form > div.form_footer > div.remember-checkbox.form_field-label.ctnr-field-label > label > span').text == '记住我的账号'
    def test_TUMIUAT_424(self):
        new_find_element(self.driver,zhuce_denglu).click()
        time.sleep(1)
        new_find_element(self.driver, username).send_keys('17316565325')
        new_find_element(self.driver, password).send_keys('gxjy5411')
        new_find_element(self.driver, denglu).click()
        time.sleep(2)
        assert self.driver.find_element_by_css_selector('#tm-login-form > div.form_error-message-container.active > div').text == '你的用户名或密码不正确。'