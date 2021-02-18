# @Author ：黄贝尔
# @Time ：2021/2/18__10:40
# #coding:utf-8
from base_page import page
import time

class product_details_page(page):

    #PDP-二级分类面包屑
    s_crumbs = ('xpath','//body/div[1]/main[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]')

    # PDP-一级分类面包屑
    f_crumbs = ('xpath', '/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]')

    #二级分类下的标题
    s_type_title = ('xpath','/html[1]/body[1]/div[1]/main[1]/div[4]/div[2]/div[1]/div[1]/div[1]/h1[1]/span[1]')

    #PDP-分享-微博
    share_blog=('xpath','//body/div[1]/main[1]/div[3]/div[1]/div[2]/div[1]/div[5]/div[3]/form[1]/div[2]/div[3]/a[2]/div[1]')

    # PDP-分享-微信
    share_wechat = ('xpath', "//body/div[1]/main[1]/div[3]/div[1]/div[2]/div[1]/div[5]/div[3]/form[1]/div[2]/div[3]/a[1]/div[1]")

    #PDP-分享-微信文案
    wechat_text=('xpath',"//h4[contains(text(),'微信扫一扫')]")
    def __init__(self,driver):
        page.__int__(self, driver)

    def click_f_crumbs(self):
        self.click(self.f_crumbs)

    def click_s_crumbs(self):
        self.click(self.s_crumbs)

    def click_share_blog(self):
        self.click(self.share_blog)
        self.new_page()

    def action_share_wechat(self):
        self.action(self.share_wechat)

