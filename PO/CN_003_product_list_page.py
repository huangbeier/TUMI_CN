# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-02-15
from base_page import page
import time
from CN_001_homepage import homepage

class product_list(page):
    # 首页-一级标签-查看全部
    all_product = ('xpath', '//body/div[1]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]')
    #首页-一级标签-旅行箱
    f_luggage=('xpath','//body/div[2]/section[1]/nav[1]/ul[1]/div[1]/li[2]/a[1]')
    #首页-一级标签-背包
    f_backpack=('xpath','//body/div[2]/section[1]/nav[1]/ul[1]/div[1]/li[3]/a[1]')
    #首页-一级标签-包袋
    f_bag=('xpath','//body/div[2]/section[1]/nav[1]/ul[1]/div[1]/li[4]/a[1]')
    #首页-一级标签-钱包及配件
    f_accessories=('xpath','//body/div[2]/section[1]/nav[1]/ul[1]/div[1]/li[5]/a[1]')
    #首页-一级标签-系列
    f_series=('xpath','//body/div[2]/section[1]/nav[1]/ul[1]/div[1]/li[6]/a[1]')
    #首页-一级标签-环保产品
    f_Environmental_protection_product=('xpath',"//a[contains(text(),'环保产品')]")
    # 首页-一级标签-个性化定制
    f_diy = ('xpath', '//body/div[2]/section[1]/nav[1]/ul[1]/div[1]/li[8]/a[1]')
    # 首页-一级标签-礼物推荐
    f_recommended = ('xpath', '//body/div[2]/section[1]/nav[1]/ul[1]/div[1]/li[9]/a[1]')
    #一级页面旅行箱-首页面包屑
    f_homepage=('xpath',"//span[contains(text(),'首页')]")
    #一级页面-旅行箱-二级标签立即购买
    s_luggage_buy=('xpath','//body/div[1]/main[1]/div[2]/div[1]/div[4]/ul[1]/li[1]/div[1]/a[2]')
    #二级页面-登机箱
    s_luggage_title=('xpath',"//span[contains(text(),'登机箱 - 旅行拉杆箱')]")
    #二级页面-第一个产品比较框
    f_compare=('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/label[1]')
    # 二级页面-第二个产品比较框
    s_compare=('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/label[1]')
    # 二级页面-第三个产品比较框
    t_compare=('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/label[1]')
    # 二级页面-第四个产品比较框
    fo_compare=('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/label[1]')
    #二级页面-比较框文本
    compare_text=('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[2]')
    #二级页面-立即比较文本
    immediately_to_compare=('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[3]/a[1]')
    #二级页面-比较报错
    compare_error =('xpath','//body/div[1]/main[1]/div[2]/div[1]')
    #二级页面-隐藏筛选
    hide_the_screening = ('xpath',"//span[contains(text(),'隐藏筛选')]")
    #二级页面-筛选-系列
    screening_series = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/h4[1]/a[1]')
    # 二级页面-筛选-颜色组
    screening_color = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/h4[1]/a[1]')
    # 二级页面-筛选-价格
    screening_prices = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/h4[1]/a[1]')
    # 二级页面-筛选-材料
    screening_material = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[4]/h4[1]/a[1]')
    # 二级页面-筛选-性别
    screening_sex = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[5]/h4[1]/a[1]')
    # 二级页面-筛选-专属功能
    screening_function = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[6]/h4[1]/a[1]')
    # 二级页面-筛选-电脑尺寸
    screening_size = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[7]/h4[1]/a[1]')
    # 二级页面-筛选-产品类型
    screening_type = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[8]/h4[1]/a[1]')
    # 二级页面-筛选-行李箱尺寸
    screening_luggage_size = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[9]/h4[1]/a[1]')
    # 二级页面-筛选-滚轮数量
    screening_roller = ('xpath','//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[10]/h4[1]/a[1]')

    def __init__(self,driver):
        page.__int__(self, driver)

    def click_f_homepage(self):
        self.click(self.f_homepage)

    def click_f_luggage(self):
        self.click(self.f_luggage)

    def click_all_product(self):
        self.click(self.all_product)
        self.new_page()

    def click_f_backpack(self):
        self.click(self.f_backpack)

    def click_f_bag(self):
        self.click(self.f_bag)

    def click_f_accessories(self):
        self.click(self.f_accessories)

    def click_f_series(self):
        self.click(self.f_series)

    def click_f_Environmental_protection_product(self):
        self.click(self.f_Environmental_protection_product)

    def click_f_diy(self):
        self.click(self.f_diy)

    def click_f_recommended(self):
        self.click(self.f_recommended)

    def click_s_luggage_buy(self):
        self.click(self.s_luggage_buy)

    def click_f_compare(self):
        self.click(self.f_compare)

    def click_s_compare(self):
        self.click(self.s_compare)

    def click_t_compare(self):
        self.click(self.t_compare)

    def click_fo_compare(self):
        self.click(self.fo_compare)

