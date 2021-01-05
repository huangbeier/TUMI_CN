# @Author ：黄贝尔
# @Time ：2020/12/4__15:01

import unittest
from selenium import webdriver
import time
from utils.seleniumtools import new_find_element
from config_moblie import host,kefu_url,chromeDriver_Path
from PO.tumi_club__moblie import huiyuan_zhuanshuliyv
from PO.store_locato_moblier import mendianleixing
from PO.cart_moblie import empty_gouwuche
from PO.HOME_PAGE_moblie import yijicaidan,lvxingxiang,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,gouwuche,sousuo,sousuo_anniu,username,password,denglu,close_login,huiyuanjulebu
from selenium.webdriver import ActionChains  #实现鼠标悬停
from selenium.webdriver.chrome.options import Options

class test_homepage_nologin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('headless')  # 以后台运行
        mobile_emulation = {"deviceName": "iPhone X"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        cls.driver = webdriver.Chrome(executable_path=chromeDriver_Path,chrome_options=options)
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        self.driver.get(f'{host}')
        time.sleep(2)
    def test_TUMIUAT_923_1(self):
        new_find_element(self.driver,yijicaidan).click()
        assert new_find_element(self.driver,lvxingxiang).text == '旅行箱'
    def test_TUMIUAT_925_1(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver, zhuce_denglu).click()
        new_find_element(self.driver, username).send_keys('17316565325')
        new_find_element(self.driver, password).send_keys('gxjy541')
        time.sleep(2)
        new_find_element(self.driver, denglu).click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="tm-panel-login-confirmation"]/div/div/ul[1]/li[1]/a').text == '查看个人信息'
    def test_TUMIUAT_925_2(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver, zhuce_denglu).click()
        new_find_element(self.driver, username).send_keys('17316565325')
        new_find_element(self.driver, password).send_keys('gxjy541')
        time.sleep(2)
        new_find_element(self.driver, denglu).click()
        time.sleep(1)
        new_find_element(self.driver,close_login).click()
        time.sleep(2)
        new_find_element(self.driver, yijicaidan).click()
        self.driver.find_element_by_xpath('//*[@id="navMainCntr"]/ul/li/ul/li[1]/div/a[2]').click()
        new_find_element(self.driver, yijicaidan).click()
        time.sleep(1)
        assert new_find_element(self.driver, zhuce_denglu).text == "登录/注册"
    def test_TUMIUAT_927_1(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver,xianxiamendian).click()
        assert new_find_element(self.driver,mendianleixing).text == '门店类型'
        assert self.driver.current_url == f'{host}/store-locator/'
    def test_TUMIUAT_928_1(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver,zaixiankefu).click()
        time.sleep(1)
        assert self.driver.current_url == kefu_url
        assert new_find_element(self.driver,tishi).text == '您好，有什么可以帮您。'
    def test_TUMIUAT_930_1(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver,huiyuanjulebu).click()
        assert self.driver.current_url == f'{host}/tumi-club/'
        assert new_find_element(self.driver,huiyuan_zhuanshuliyv).text == '会员专属礼遇'
    def test_TUMIUAT_931(self):
        self.driver.find_element_by_xpath('//*[@id="top-nav"]/header/div[3]/div[4]/div[4]/div/a/span[1]').click()
        new_find_element(self.driver,sousuo).send_keys('alp')
        new_find_element(self.driver,sousuo_anniu).click()
        time.sleep(1)
        assert self.driver.find_element_by_css_selector('#productTabContent > div.page-title-compare-cntr > div > div.page-title-breadcrum > h1').text == '搜索页'
    def test_TUMIUAT_935(self):
        self.driver.find_element_by_xpath('//*[@id="top-nav"]/header/div[3]/div[4]/div[4]/div/a/span[1]').click()
        new_find_element(self.driver, sousuo).send_keys('alpp')
        new_find_element(self.driver, sousuo_anniu).click()
        time.sleep(1)
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[2]/div[2]/div/div[1]').text == '尝试新的搜索'
    # def test_TUMIUAT_412_1(self):
    #     new_find_element(self.driver, sousuo).send_keys('alp')
    #     ActionChains(self.driver).move_to_element(new_find_element(self.driver,sousuo)).perform()#鼠标悬停到搜索框
    #     time.sleep(5)
    #     assert self.driver.find_element_by_xpath('//*[@id="suggested_categories"]/span/a').text == 'alpha'
    # def test_TUMIUAT_413_1(self):
    #     new_find_element(self.driver, sousuo).send_keys('alp')
    #     ActionChains(self.driver).move_to_element(new_find_element(self.driver, sousuo)).perform()  # 鼠标悬停到搜索框
    #     time.sleep(5)
    #     self.driver.find_element_by_xpath('//*[@id="matching_products"]/li[1]/a/span[2]/span[1]').click()
    #     assert self.driver.find_element_by_xpath('//*[@id="prod-details"]/h1').text == 'Lance双肩包'