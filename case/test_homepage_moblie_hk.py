# @Author ：黄贝尔
# @Time ：2020/12/4__15:01

import unittest
from selenium import webdriver
import time
from utils.seleniumtools import new_find_element
from config_moblie_hk import host,kefu_url,chromeDriver_Path
from PO.tumi_club_moblie_hk import huiyuan_zhuanshuliyv
from PO.store_locator_moblie_hk import mendianleixing
from PO.HOME_PAGE_moblie_hk import yijicaidan,lvxingxiang,zhuce_denglu,xianxiamendian,zaixiankefu,\
    sousuo,sousuo_anniu,username,password,denglu,close_login,huiyuanjulebu,fenlei_lvxingxiang,fenlei_recycled,\
    fenlei_peijian,fenlei_xiekuabao,fenlei_tuotebao,fenlei_beibao
from selenium.webdriver import ActionChains  #实现鼠标悬停
from selenium.webdriver.chrome.options import Options
class test_homepage_nologin1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('headless')#以后台运行
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
        # self.driver.set_page_load_timeout(10)# 设定页面加载限制时间
        # self.driver.execute_script('window.stop()')# 超时报错后就强制停止加载
        time.sleep(2)
    def test_TUMIUAT_1128_1(self):
        new_find_element(self.driver,yijicaidan).click()
        assert new_find_element(self.driver,lvxingxiang).text == 'LUGGAGE'
    def test_TUMIUAT_1130_1(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver, zhuce_denglu).click()
        new_find_element(self.driver, username).send_keys('67969782')
        new_find_element(self.driver, password).send_keys('Tumi_2019')
        time.sleep(2)
        new_find_element(self.driver, denglu).click()
        time.sleep(3)
        assert self.driver.find_element_by_xpath('//*[@id="tm-panel-login-confirmation"]/header/h3').text == 'My Account'
    def test_TUMIUAT_1130_2(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver, zhuce_denglu).click()
        new_find_element(self.driver, username).send_keys('67969782')
        new_find_element(self.driver, password).send_keys('Tumi_2019')
        time.sleep(2)
        new_find_element(self.driver, denglu).click()
        time.sleep(1)
        new_find_element(self.driver,close_login).click()
        time.sleep(2)
        new_find_element(self.driver, yijicaidan).click()
        self.driver.find_element_by_xpath('//*[@id="navMainCntr"]/ul/li/ul/li[1]/div/a[2]').click()
        time.sleep(1)
        new_find_element(self.driver, yijicaidan).click()
        time.sleep(5)
        assert new_find_element(self.driver, zhuce_denglu).text == 'Login / Register'
    def test_TUMIUAT_1133_1(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver,xianxiamendian).click()
        assert new_find_element(self.driver,mendianleixing).text == 'Store Type'
        assert self.driver.current_url == f'{host}/store-locator/'
    def test_TUMIUAT_1134_1(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver,zaixiankefu).click()
        time.sleep(1)
        assert self.driver.current_url == kefu_url
    def test_TUMIUAT_1132_1(self):
        new_find_element(self.driver, yijicaidan).click()
        new_find_element(self.driver,huiyuanjulebu).click()
        assert self.driver.current_url == f'{host}/tumi-exclusives-club/'
        assert new_find_element(self.driver,huiyuan_zhuanshuliyv).text == 'Member Privilege'
    def test_TUMIUAT_1136(self):
        self.driver.find_element_by_xpath('//*[@id="top-nav"]/header/div[3]/div[4]/div[4]/div/a/span[1]').click()
        new_find_element(self.driver, sousuo).send_keys('alp')
        new_find_element(self.driver, sousuo_anniu).click()
        time.sleep(1)
        assert self.driver.find_element_by_css_selector(
            '#productTabContent > div.page-title-compare-cntr > div > div.page-title-breadcrum > h1').text == 'search page'
    def test_TUMIUAT_935(self):
        self.driver.find_element_by_xpath('//*[@id="top-nav"]/header/div[3]/div[4]/div[4]/div/a/span[1]').click()
        new_find_element(self.driver, sousuo).send_keys('alpp')
        new_find_element(self.driver, sousuo_anniu).click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[2]/div[2]/div/div[1]').text == 'TRY A NEW SEARCH'
    def test_TUMIUAT_1138(self):
        self.driver.find_element_by_xpath('//*[@id="top-nav"]/header/div[3]/div[4]/div[4]/div/a/span[1]').click()
        new_find_element(self.driver, sousuo).send_keys('alp')
        ActionChains(self.driver).move_to_element(new_find_element(self.driver, sousuo)).perform()  # 鼠标悬停到搜索框
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="matching_products"]/li[1]/a/span[2]/span[1]').click()
        # js = "window.scrollTo(0,300);"
        # self.driver.execute_script(js)#向下滑动多少像素
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//h3[contains(text(),'Quantity:')]").text == 'QUANTITY:'
    def test_TUMIUAT_1139(self):
        self.driver.find_element_by_xpath('//*[@id="top-nav"]/header/div[3]/div[4]/div[4]/div/a/span[1]').click()
        new_find_element(self.driver, sousuo).send_keys('alp')
        ActionChains(self.driver).move_to_element(new_find_element(self.driver, sousuo)).perform()  # 鼠标悬停到搜索框
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[contains(text(),'View all results')]").click()
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//h1[contains(text(),'search page')]").text == 'search page'
    def test_TUMIUAT_1143_1(self):
        new_find_element(self.driver,fenlei_lvxingxiang).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(4)
        assert self.driver.current_url == f'{host}/c-luggage/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'All Luggage, from Checked Bags to Backpacks'
    def test_TUMIUAT_1143_2(self):
        new_find_element(self.driver,fenlei_beibao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-backpacks/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'Leather Backpacks & Sling Bags'
    def test_TUMIUAT_1143_3(self):
        new_find_element(self.driver,fenlei_tuotebao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-bag/totes/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'Tote Bags for Men & Women'
    def test_TUMIUAT_1143_4(self):
        new_find_element(self.driver,fenlei_xiekuabao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-bag/crossbodies/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'Cross Body Bags, Carry On Luggage & Totes'
    def test_TUMIUAT_1143_5(self):
        new_find_element(self.driver,fenlei_peijian).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-accessories/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'All Accessories, Electronics, Wallets & Money Clips'
    def test_TUMIUAT_1143_6(self):
        new_find_element(self.driver,fenlei_recycled).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-collections/recycled/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == "Men's & Women's styles made from recycled materials"