# @Author ：黄贝尔
# @Time ：2021/1/6__11:41
# #coding:utf-8
import unittest
from selenium import webdriver
import time
from utils.seleniumtools import new_find_element
from config_hk import host,kefu_url,chromeDriver_Path
from PO.tumi_club_hk import huiyuan_zhuanshuliyv
from PO.store_locator_hk import mendianleixing
from PO.HOME_PAGE_hk import lvxingxiang,huiyuanjulebu,zhuce_denglu,xianxiamendian,zaixiankefu,\
    tishi,gouwuche,denglu,jixv_gouwu,username,password,close_login,gerenxinxi
from PO.my_account_hk import mb_gerenxinxi,mb_gengxingerenxinxi,mb_gengxinmima,mb_dizhibu,geren_baocun,\
    geren_username,geren_qingxuanze,geren_chenghu



class test_My_Account_hk(unittest.TestCase):
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
        # self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(5)
        flag = self.driver.find_elements_by_link_text('Login / Register')
        if len(flag) == 1:
            new_find_element(self.driver, zhuce_denglu).click()
            time.sleep(1)
            new_find_element(self.driver, username).send_keys('67969782')
            new_find_element(self.driver, password).send_keys('Tumi_2019')
            time.sleep(2)
            new_find_element(self.driver, denglu).click()
            time.sleep(2)
            new_find_element(self.driver, gerenxinxi).click()
            # new_find_element(self.driver, close_login).click()
            # self.driver.refresh()  # 登陆完后刷新页面
            # time.sleep(1)
        else:
            pass
    def test_TUMIUAT_821_822(self):
        new_find_element(self.driver,gerenxinxi).click()
        time.sleep(3)
        assert new_find_element(self.driver,mb_gerenxinxi).text == 'Personal Information'
        assert self.driver.current_url == f'{host}/my-account/profile'
        assert new_find_element(self.driver,mb_dizhibu).text == 'MY ADDRESS BOOK'
        assert new_find_element(self.driver, mb_gengxinmima).text == 'UPDATE PASSWORD'
        assert new_find_element(self.driver, mb_gengxingerenxinxi).text == 'Update Personal Information'
    def test_TUMIUAT_825(self):
        new_find_element(self.driver,mb_gengxingerenxinxi).click()
        new_find_element(self.driver,geren_username).clear()
        new_find_element(self.driver,geren_baocun).click()
        time.sleep(2)
        assert self.driver.find_element_by_id('userName.errors').text == 'Please enter a username.'
    def test_TUMIUAT_1604(self):
        new_find_element(self.driver,mb_gengxingerenxinxi).click()
        new_find_element(self.driver,geren_chenghu).click()
        new_find_element(self.driver, geren_qingxuanze).click()
        new_find_element(self.driver, geren_baocun).click()
        time.sleep(2)
        assert self.driver.find_element_by_id('titleCode.errors').text == 'Please choose your title.'
    def test_TUMIUAT_1605(self):
        new_find_element(self.driver,mb_gengxingerenxinxi).click()
        new_find_element(self.driver,geren_chenghu).click()
        self.driver.find_element_by_css_selector('#profile\.titleSelectBoxItOptions > li.selectboxit-option.selectboxit-focus > a').click()
        new_find_element(self.driver, geren_baocun).click()
        time.sleep(2)
        assert new_find_element(self.driver, mb_gengxingerenxinxi).text == 'Update Personal Information'