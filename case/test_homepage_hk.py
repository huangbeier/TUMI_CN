# @Author ：黄贝尔
# @Time ：2020/12/4__15:01

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities#21行引用
import time
from utils.seleniumtools import new_find_element
from config_hk import host,kefu_url,chromeDriver_Path
from PO.tumi_club_hk import huiyuan_zhuanshuliyv
from PO.store_locator_hk import mendianleixing
from PO.cart_hk import empty_gouwuche
from PO.HOME_PAGE_hk import lvxingxiang,huiyuanjulebu,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,gouwuche,sousuo,sousuo_anniu,fenlei_recycled,fenlei_peijian,fenlei_xiekuabao,fenlei_tuotebao,fenlei_beibao,\
    fenlei_lvxingxiang
from selenium.webdriver import ActionChains  #实现鼠标悬停


class test_homepage_nologin_hk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('- -disable - infobars')
        option.add_argument('–window - size = 1024, 1024')
        option.add_argument('- headless')  # 以后台运行
        cls.driver = webdriver.Chrome(executable_path=chromeDriver_Path)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
        self.driver.get(f'{host}')
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(20)# 设定页面加载限制时间
        self.driver.execute_script('window.stop()')# 超时报错后就强制停止加载
        time.sleep(2)
    def test_TUMIUAT_662_1(self):
        assert new_find_element(self.driver,lvxingxiang).text == 'LUGGAGE'
        assert new_find_element(self.driver,huiyuanjulebu).text == 'TUMI Exclusives Club'
        assert new_find_element(self.driver,zhuce_denglu).text == 'Login / Register'
    def test_TUMIUAT_662_2(self):
        new_find_element(self.driver, huiyuanjulebu).click()
        #self.driver.window_handles()#获取N个网页句柄
        self.driver.switch_to_window(self.driver.window_handles[-1])#切换到最新的网页
        assert self.driver.current_url == f'{host}/tumi-exclusives-club/'
        assert new_find_element(self.driver,huiyuan_zhuanshuliyv).text == 'Member Privilege'
    def test_TUMIUAT_662_3(self):
        new_find_element(self.driver,xianxiamendian).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{host}/store-locator/'
        assert new_find_element(self.driver,mendianleixing).text == 'Store Type'
    def test_TUMIUAT_662_4(self):
        new_find_element(self.driver,zaixiankefu).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{kefu_url}'
        assert new_find_element(self.driver,tishi).text == "It's non working time now. Should you have enquiry, please leave msg. Thank you!"
    def test_TUMIUAT_662_5(self):
        new_find_element(self.driver,gouwuche).click()
        assert self.driver.current_url ==f'{host}/cart'
        assert new_find_element(self.driver,empty_gouwuche).text == 'Shopping cart is empty'
    def test_TUMIUAT_662_6(self):
        new_find_element(self.driver,zhuce_denglu).click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="tm-panel-login"]/div[2]/h4').text == 'Still no TUMI account?'
    def test_TUMIUAT_664_1(self):
        new_find_element(self.driver,sousuo).send_keys('alp')
        new_find_element(self.driver,sousuo_anniu).click()
        assert self.driver.find_element_by_xpath('//*[@id="productTabContent"]/div[1]/div/div[1]/h1').text == 'search page'
    def test_TUMIUAT_665_1(self):
        new_find_element(self.driver, sousuo).send_keys('alpp')
        new_find_element(self.driver, sousuo_anniu).click()
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[2]/div[1]/div/div[1]').text == 'SORRY, NO SEARCH RESULTS'
    def test_TUMIUAT_666_1(self):
        new_find_element(self.driver, sousuo).send_keys('alp')
        ActionChains(self.driver).move_to_element(new_find_element(self.driver,sousuo)).perform()#鼠标悬停到搜索框
        time.sleep(5)
        assert self.driver.find_element_by_xpath('//*[@id="suggested_categories"]/span/a').text == 'alpha'
    def test_TUMIUAT_667_1(self):
        new_find_element(self.driver, sousuo).send_keys('alp')
        ActionChains(self.driver).move_to_element(new_find_element(self.driver, sousuo)).perform()  # 鼠标悬停到搜索框
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="matching_products"]/li[1]/a/span[2]/span[1]').click()
        assert self.driver.find_element_by_xpath('//*[@id="prod-details"]/h1').text == 'McCoy Gym Bag'
    def test_TUMIUAT_1521_1(self):
        new_find_element(self.driver,fenlei_lvxingxiang).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(1)
        assert self.driver.current_url == f'{host}/c-luggage/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'All Luggage, from Checked Bags to Backpacks'
    def test_TUMIUAT_1521_2(self):
        new_find_element(self.driver,fenlei_beibao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-backpacks/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'Leather Backpacks & Sling Bags'
    def test_TUMIUAT_1521_3(self):
        new_find_element(self.driver,fenlei_tuotebao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-bag/totes/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'Tote Bags for Men & Women'

    def test_TUMIUAT_1521_4(self):
        new_find_element(self.driver, fenlei_xiekuabao).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-bag/crossbodies/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'Cross Body Bags, Carry On Luggage & Totes'
    def test_TUMIUAT_1521_5(self):
        new_find_element(self.driver, fenlei_peijian).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-accessories/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath(
            '//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == 'All Accessories, Electronics, Wallets & Money Clips'
    def test_TUMIUAT_1521_6(self):
        new_find_element(self.driver,fenlei_recycled).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        time.sleep(2)
        assert self.driver.current_url == f'{host}/c-collections/recycled/?q=:relevance&pageSize=30&page=0&sort=relevance'
        assert self.driver.find_element_by_xpath('//*[@id="navEnd"]/div[4]/div[2]/div[1]/div/div[1]/h1/span[1]').text == "Men's & Women's styles made from recycled materials"