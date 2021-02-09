# @Author ：黄贝尔
# @Time ：2021/2/7__13:39
# #coding:utf-8
from base_page import page
import time

class homepage(page):
    #中心LOGO
    logo=('xpath','//body/div[2]/section[1]/div[4]/div[1]/a[1]/img[1]')
    #会员俱乐部
    vip_club=('xpath','//header/div[3]/div[2]/a[1]')
    #微信精品店
    wechat=('xpath','//header/div[3]/div[2]/a[2]')
    #线下门店
    offline_store=('xpath','//header/div[3]/div[2]/a[3]')
    #在线客服
    customer_service=('xpath','//header/div[3]/div[2]/a[4]')
    #购物车
    cart=('id',"minicart_data")
    #登陆注册
    login_register_btn=('link text','登录/注册')
    #手机号
    phone=('id','j_username')
    #密码
    password=('id','j_password')
    #登录按钮
    login_btn=('id','login-option-regular')
    #搜索框
    search=('id','search')
    #悬浮框-建议关键字
    keyword = ('xpath', "//h4[@id='suggested_categories_header']")
    #首页-登陆后的用户名
    my_username=('xpath',"//header/div[3]/div[3]/div[3]/a[1]")
    #关闭登录
    close_login=('xpath',"//body[1]/div[2]/div[2]/div[2]/div[1]/div[4]/header[1]/a[1]/span[1]")
    #搜索按钮
    search_btn=('xpath','//body/div[2]/section[1]/div[5]/div[2]/form[1]/div[1]/button[1]')
    #建议关键字
    suggested_keyword=('xpath',"//a[contains(text(),'alpha')]")
    #分类广告位-旅行箱
    f_luggage=('id',"luggage")
    #分类广告位-背包
    f_backpacks=('id','backpacks')
    #分类广告位-托特包
    f_crossbodies=('id','crossbodies')
    #分类广告位-斜挎包
    f_totes=('id','totes')
    #分类广告位-钱包与配件
    f_accessories=('id','accessories')
    #分类广告位-环保产品
    f_recycled=('id','recycled')
    #底部广告位-标题
    bottom_AD_space_title=('xpath','//body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[2]/a[1]/h3[1]')
    #底部广告位-即可探索
    bottom_AD_space_explore=('xpath',"//body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[2]/a[1]/div[1]")
    # 底部广告位-图片
    bottom_AD_space_img=('xpath',"//body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/img[1]")
    # 底部广告位-标题 右边的那个
    bottom_AD_space_title2 = ('xpath', '//body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[2]/a[1]/h3[1]')
    #底部广告位-即可探索 右边的那个
    bottom_AD_space_explore2=('xpath',"//body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[2]/a[1]/div[1]")
    # 底部广告位-图片 右边的那个
    bottom_AD_space_img2=('xpath',"//body/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/a[1]/img[1]")
    #登出
    sign_out_btn=('link text','登出')

    def __init__(self,driver):
        page.__int__(self, driver)

    def login(self):
        self.click(self.login_register_btn)
        time.sleep(1)
        self.input_text(self.phone,text='17316565325')
        self.input_text(self.password,text='gxjy541')
        self.click(self.login_btn)
        time.sleep(1)
        self.click(self.close_login)
        time.sleep(0.5)

    def sign_out(self):
        self.click(self.sign_out_btn)

    def login_no_phone(self):
        self.click(self.login_register_btn)
        time.sleep(1)
        self.input_text(self.password,text='gxjy541')
        self.click(self.login_btn)
        time.sleep(1)

    def login_phone_error(self):
        self.click(self.login_register_btn)
        time.sleep(1)
        self.input_text(self.phone, text='17316565329')
        self.input_text(self.password,text='gxjy541')
        self.click(self.login_btn)
        time.sleep(1)

    def login_no_password(self):
        self.click(self.login_register_btn)
        time.sleep(1)
        self.input_text(self.phone, text='17316565325')
        self.click(self.login_btn)
        time.sleep(1)

    def login_password_error(self):
        self.click(self.login_register_btn)
        time.sleep(1)
        self.input_text(self.phone, text='17316565325')
        self.input_text(self.password,text='gxjy5411')
        self.click(self.login_btn)
        time.sleep(1)

    def click_logo(self):
        self.click(self.logo)

    def click_vip_club(self):
        self.click(self.vip_club)
        self.new_page()

    def move_to_wechat(self):
        self.action(self.wechat)

    def click_offline_store(self):
        self.click(self.offline_store)
        self.new_page()

    def click_customer_service(self):
        self.click(self.customer_service)
        self.new_page()

    def click_cart(self):
        self.click(self.cart)
        self.new_page()

    def click_login(self):
        self.click(self.login_register_btn)

    def click_my_username(self):
        self.click(self.my_username)

    def search_for_Effective_Products(self):
        self.input_text(self.search,text='alp')
        self.action(self.search)
    def click_suggested_keyword(self):
        self.click(self.suggested_keyword)
        time.sleep(1)

    def Search_for_Invalid_Products(self):
        self.input_text(self.search,text='alpp')
        self.click(self.search_btn)
        self.new_page()

    def click_f_luggage(self):
        self.click(self.f_luggage)
        self.new_page()

    def click_f_backpacks(self):
        self.click(self.f_backpacks)
        self.new_page()

    def click_f_crossbodies(self):
        self.click(self.f_crossbodies)
        self.new_page()

    def click_f_totes(self):
        self.click(self.f_totes)
        self.new_page()

    def click_f_accessories(self):
        self.click(self.f_accessories)
        self.new_page()

    def click_f_recycled(self):
        self.click(self.f_recycled)
        self.new_page()

    def roll_to_bottom_AD_space(self):
        self.roll_to_element(3000)
        time.sleep(2)

    def click_bottom_AD_space_title(self):
        self.click(self.bottom_AD_space_title)

    def click_bottom_AD_space_title2(self):
        self.click(self.bottom_AD_space_title2)

    def click_bottom_AD_space_explore(self):
        self.click(self.bottom_AD_space_explore)

    def click_bottom_AD_space_explore2(self):
        self.click(self.bottom_AD_space_explore2)

    def click_bottom_AD_space_img(self):
        self.click(self.bottom_AD_space_img)

    def click_bottom_AD_space_img2(self):
        self.click(self.bottom_AD_space_img2)



