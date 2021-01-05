# @Author ：黄贝尔
# @Time ：2021/1/4__11:02
# #coding:utf-8
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.seleniumtools import new_find_element
from config_hk import host,kefu_url,chromeDriver_Path
from PO.tumi_club_hk import huiyuan_zhuanshuliyv
from PO.store_locator_hk import mendianleixing
from PO.HOME_PAGE_hk import lvxingxiang,huiyuanjulebu,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,gouwuche,denglu,jixv_gouwu,username,password,close_login,my_account1
from PO.my_account_hk import my_account


class test_homepage_login_hk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('headless')  # 以后台运行
        cls.driver = webdriver.Chrome(executable_path=chromeDriver_Path)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
        self.driver.get(f'{host}')
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(15)# 设定页面加载限制时间
        self.driver.execute_script('window.stop()')# 超时报错后就强制停止加载
        time.sleep(2)
        flag=self.driver.find_elements_by_link_text('Login / Register')
        if len(flag)==1:
            new_find_element(self.driver, zhuce_denglu).click()
            time.sleep(1)
            new_find_element(self.driver, username).send_keys('90000001')
            new_find_element(self.driver, password).send_keys('1111qqqq')
            time.sleep(2)
            new_find_element(self.driver, denglu).click()
            time.sleep(2)
            new_find_element(self.driver,close_login).click()
            self.driver.refresh()#登陆完后刷新页面
            time.sleep(1)
        else:
            pass
    def test_TUMIUAT_663_1(self):
        time.sleep(1)
        assert new_find_element(self.driver, lvxingxiang).text == 'LUGGAGE'
        assert new_find_element(self.driver, huiyuanjulebu).text == 'TUMI Exclusives Club'
    def test_TUMIUAT_663_2(self):
        new_find_element(self.driver, huiyuanjulebu).click()
        # self.driver.window_handles()#获取N个网页句柄
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{host}/tumi-exclusives-club/'
        assert new_find_element(self.driver, huiyuan_zhuanshuliyv).text == 'Member Privilege'
    def test_TUMIUAT_663_3(self):
        new_find_element(self.driver, xianxiamendian).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{host}/store-locator/'
        assert new_find_element(self.driver, mendianleixing).text == 'Store Type'
    def test_TUMIUAT_663_4(self):
        new_find_element(self.driver, zaixiankefu).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 切换到最新的网页
        assert self.driver.current_url == f'{kefu_url}'
        assert new_find_element(self.driver, tishi).text == "It's non working time now. Should you have enquiry, please leave msg. Thank you!"
    def test_TUMIUAT_663_5(self):
        new_find_element(self.driver, gouwuche).click()
        time.sleep(1)
        assert new_find_element(self.driver, jixv_gouwu).text == 'Continue shopping'
    def test_TUMIUAT_663_6(self):
        new_find_element(self.driver,my_account1).click()
        time.sleep(2)
        assert new_find_element(self.driver, my_account).text == 'My Account'
