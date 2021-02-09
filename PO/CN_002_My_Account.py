# @Author ：黄贝尔
# @Time ：2021/2/9__13:39
# #coding:utf-8
from base_page import page
import time
from CN_001_homepage import homepage

class my_account(page):

    #查看个人信息
    view_my_info=('xpath',"//body/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[1]/a[1]")
    #查看我的账号
    view_my_account=('xpath','//header/div[3]/div[3]/div[3]/a[1]')
    #更新个人信息
    update_my_info=('xpath',"//a[contains(text(),'更新个人信息')]")
    #地址簿
    my_address=('xpath',"//a[contains(text(),'我的地址簿')]")
    #更新密码
    update_my_password=('xpath',"//a[contains(text(),'更新密码')]")
    #附近门店
    nearby_stores=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/a[1]')
    #返回门店搜索
    store_search=('xpath',"//a[contains(text(),'< 返回门店搜索')]")
    #个性化输入框
    diy_Input=('id','monogram.initials')
    #个性化按钮
    diy_btn=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/span[1]')
    #更新个人信息用户名输入框
    account_username=('id','profile.userName')
    #更新个人信息称呼
    account_call =('id','profile.titleSelectBoxIt')
    #小姐称呼
    call_miss = ('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[2]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[3]/span[1]/ul[1]/li[2]/a[1]')
    #更新个人信息邮箱
    account_email=('id','profile.email')
    #更新保存按钮
    account_save_btn=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[2]/div[2]/form[1]/div[3]/button[1]')
    #个人中心logo
    account_logo=('xpath','//body/div[1]/section[1]/div[4]/div[1]/a[1]/img[1]')

    def __init__(self,driver):
        page.__int__(self, driver)
    def go_to_my_info(self):
        self.click(homepage.login_register_btn)
        time.sleep(1)
        self.input_text(homepage.phone, text='17316565325')
        self.input_text(homepage.password, text='gxjy541')
        self.click(homepage.login_btn)
        time.sleep(1)
        self.click(self.view_my_info)

    def click_account_logo(self):
        self.click(self.account_logo)

    def move_to_logo(self):
        self.action(self.account_logo)
    def go_to_my_account(self):
        homepage1=homepage(self.driver)
        homepage1.login()
        time.sleep(1)
        self.click(self.view_my_account)
        self.driver.refresh()

    def click_nearby_stores(self):
        self.click(self.nearby_stores)

    def click_store_search(self):
        self.click(self.store_search)

    def input_diy(self):
        self.input_text(self.diy_Input,text='1')

    def click_diy_btn(self):
        self.action(self.diy_btn)
        self.click(self.diy_btn)

    def click_update_my_info(self):
        self.click(self.update_my_info)

    def clear_account_username(self):
        self.clear_loc(self.account_username)

    def clear_account_email(self):
        self.clear_loc(self.account_email)

    def input_account_username(self):
        self.input_text(self.account_username,text='测试')

    def click_account_call(self):
        self.click(self.account_call)

    def click_call_miss(self):
        self.click(self.call_miss)

    def input_account_email(self):
        self.input_text(self.account_email,text='testtest@qq.com')

    def click_account_save_btn(self):
        self.click(self.account_save_btn)










