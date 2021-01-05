# @Author ：黄贝尔
# @Time ：2020/12/4__15:01

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
    fenlei_peijian,fenlei_recycled
from selenium.webdriver import ActionChains  #实现鼠标悬停

class test_homepage_nologin(unittest.TestCase):
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
    def test_TUMIUAT_408_1(self):
        assert new_find_element(self.driver,lvxingxiang).text == '旅行箱'
        assert new_find_element(self.driver,huiyuanjulebu).text == '会员俱乐部'
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
        assert self.driver.find_element_by_xpath('//*[@id="tm-panel-login"]/div[2]/h4').text == '还没有TUMI账号?'
    def test_TUMIUAT_410_1(self):
        new_find_element(self.driver,sousuo).send_keys('alp')
        new_find_element(self.driver,sousuo_anniu).click()
        assert self.driver.find_element_by_xpath('//*[@id="productTabContent"]/div[1]/div/div[1]/h1').text == '搜索页'
    def test_TUMIUAT_411_1(self):
        new_find_element(self.driver, sousuo).send_keys('alpp')
        new_find_element(self.driver, sousuo_anniu).click()
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[2]/div[1]/div/div[1]').text == '对不起，没有搜索结果'
    def test_TUMIUAT_412_1(self):
        new_find_element(self.driver, sousuo).send_keys('alp')
        ActionChains(self.driver).move_to_element(new_find_element(self.driver,sousuo)).perform()#鼠标悬停到搜索框
        time.sleep(5)
        assert self.driver.find_element_by_xpath('//*[@id="suggested_categories"]/span/a').text == 'alpha'
    def test_TUMIUAT_413_1(self):
        new_find_element(self.driver, sousuo).send_keys('alp')
        ActionChains(self.driver).move_to_element(new_find_element(self.driver, sousuo)).perform()  # 鼠标悬停到搜索框
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="matching_products"]/li[1]/a/span[2]/span[1]').click()
        assert self.driver.find_element_by_xpath('//*[@id="addToCartBtn"]').text == '添加到购物车'
    def test_TUMIUAT_1510_1(self):
        new_find_element(self.driver,fenlei_lvxingxiang).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(1)
        assert self.driver.current_url == f'{host}/c-luggage/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '各类旅行箱 - 托运旅行箱、登机箱'
    def test_TUMIUAT_1510_2(self):
        new_find_element(self.driver,fenlei_beibao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-backpacks/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '各类背包 - 商务、旅行、休闲背包'
    def test_TUMIUAT_1510_3(self):
        new_find_element(self.driver,fenlei_tuotebao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-bag/totes/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '托特包 - 手拎包、手袋'
    def test_TUMIUAT_1510_4(self):
        new_find_element(self.driver,fenlei_xiekuabao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-bag/crossbodies/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '斜挎包 - 休闲斜挎包'
    def test_TUMIUAT_1510_5(self):
        new_find_element(self.driver,fenlei_peijian).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-accessories/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '各类旅行配件、电子产品、钱包等'
    def test_TUMIUAT_1510_6(self):
        new_find_element(self.driver,fenlei_recycled).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-collections/recycled/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '由可回收材料制成的环保系列'