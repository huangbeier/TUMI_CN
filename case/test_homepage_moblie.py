# @Author ：黄贝尔
# @Time ：2020/12/4__15:01

import unittest
from selenium import webdriver
import time
from utils.seleniumtools import new_find_element
from config_moblie import host,kefu_url,chromeDriver_Path
from PO.tumi_club__moblie import huiyuan_zhuanshuliyv
from PO.store_locato_moblier import mendianleixing
from PO.HOME_PAGE_moblie import yijicaidan,lvxingxiang,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,sousuo,sousuo_anniu,username,password,denglu,close_login,huiyuanjulebu,fenlei_lvxingxiang,\
    fenlei_beibao,fenlei_tuotebao,fenlei_xiekuabao,fenlei_peijian,fenlei_recycled
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
    def test_TUMIUAT_933(self):
        self.driver.find_element_by_xpath('//*[@id="top-nav"]/header/div[3]/div[4]/div[4]/div/a/span[1]').click()
        new_find_element(self.driver, sousuo).send_keys('alp')
        ActionChains(self.driver).move_to_element(new_find_element(self.driver, sousuo)).perform()  # 鼠标悬停到搜索框
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="matching_products"]/li[1]/a/span[2]/span[1]').click()
        assert self.driver.find_element_by_xpath('//*[@id="addToCartBtn"]').text == '添加到购物车'
    def test_TUMIUAT_934(self):
        self.driver.find_element_by_xpath('//*[@id="top-nav"]/header/div[3]/div[4]/div[4]/div/a/span[1]').click()
        new_find_element(self.driver, sousuo).send_keys('alp')
        ActionChains(self.driver).move_to_element(new_find_element(self.driver, sousuo)).perform()  # 鼠标悬停到搜索框
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[contains(text(),'查看所有结果')]").click()
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//h1[contains(text(),'搜索页')]").text == '搜索页'
    def test_TUMIUAT_938_1(self):
        js = "window.scrollTo(0,600);"
        self.driver.execute_script(js)#向下滑动多少像素
        new_find_element(self.driver,fenlei_lvxingxiang).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(1)
        assert self.driver.current_url == f'{host}/c-luggage/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '各类旅行箱 - 托运旅行箱、登机箱'
    def test_TUMIUAT_938_2(self):
        new_find_element(self.driver,fenlei_beibao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-backpacks/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '各类背包 - 商务、旅行、休闲背包'
    def test_TUMIUAT_938_3(self):
        new_find_element(self.driver,fenlei_tuotebao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-bag/totes/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '托特包 - 手拎包、手袋'
    def test_TUMIUAT_938_4(self):
        new_find_element(self.driver,fenlei_xiekuabao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-bag/crossbodies/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '斜挎包 - 休闲斜挎包'
    def test_TUMIUAT_938_5(self):
        new_find_element(self.driver,fenlei_peijian).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-accessories/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '各类旅行配件、电子产品、钱包等'
    def test_TUMIUAT_938_6(self):
        new_find_element(self.driver,fenlei_recycled).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-collections/recycled/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == '由可回收材料制成的环保系列'
