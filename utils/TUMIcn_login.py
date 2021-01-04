# @Author ：黄贝尔
# @Time ：2021/1/4__9:41
# #coding:utf-8

from selenium import webdriver
from config import chromeDriver_Path,host
from PO.HOME_PAGE import zhuce_denglu,username,password,denglu
from utils.seleniumtools import new_find_element
import time
driver=webdriver.Chrome(executable_path=chromeDriver_Path)
def login():
    # driver.get(f'{host}')
    # driver.maximize_window()
    new_find_element(driver,zhuce_denglu).click()
    new_find_element(driver,username).send_keys('17316565325')
    new_find_element(driver,password).send_keys('gxjy541')
    time.sleep(2)
    new_find_element(driver,denglu).click()

# login()




