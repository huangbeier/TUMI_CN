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
    #PDP-现在添加
    diy_add = ('xpath',"//a[contains(text(),'现在添加')]")
    #PDP-diy-第一个字符
    diy_firstNum=('xpath','//body/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
    #PDP-diy-默认diy勾选框
    diy_default = ('id','setDefault')
    #PDP-diy第一步-下一步
    diy_f_next = ('xpath','//body/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[3]/a[1]')
    #PDP-diy第二步-下一步
    diy_s_next = ('xpath','//body/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[3]/a[2]')
    # PDP-diy第二步-上一步
    diy_s_before = ('xpath', '//body/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[3]/a[1]')
    # PDP-diy第三部-上一步
    diy_t_before = ('xpath','//body/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[3]/a[1]')
    #PDP-diy第三部-成功
    diy_t_ok = ('xpath',"//a[contains(text(),'申请个性定制')]")
    #PDP-diy-编辑
    diy_edit=('xpath',"//a[contains(text(),'编辑')]")
    # PDP-diy-删除
    diy_del = ('xpath', "//a[contains(text(),'移除')]")

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

    def click_diy_add(self):
        self.click(self.diy_add)

    def input_diy_firstNum(self):
        self.input_text(self.diy_firstNum,text='1')

    def input_diy_firstNum2(self):
        self.input_text(self.diy_firstNum,text='2')

    def clear_diy_firstNum(self):
        self.clear_loc(self.diy_firstNum)

    def click_diy_default(self):
        self.click(self.diy_default)

    def click_diy_f_next(self):
        self.click(self.diy_f_next)

    def click_diy_s_next(self):
        self.click(self.diy_s_next)

    def click_diy_s_before(self):
        self.click(self.diy_s_before)

    def click_diy_t_before(self):
        self.click(self.diy_t_before)

    def click_diy_t_ok(self):
        self.click(self.diy_t_ok)

    def click_diy_edit(self):
        self.click(self.diy_edit)

    def click_diy_del(self):
        self.click(self.diy_del)

