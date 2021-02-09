# @Author ：黄贝尔
# @Time ：2021/2/7__14:23
# #coding:utf-8
class homepage_assert_element():
    vip_Privilege=('xpath',"//strong[contains(text(),'会员专属礼遇')]")
    wechat_text=('xpath','//header/div[3]/div[2]/a[2]/div[1]/div[2]/p[1]')
    store_type=('xpath',"//div[contains(text(),'门店类型')]")
    login_text=('xpath',"//span[contains(text(),'登录您的TUMI.CN账号')]")
    no_search=('xpath',"//div[contains(text(),'对不起，没有搜索结果')]")
    have_search=('xpath',"//div[contains(text(),'搜索结果')]")
    luggage_title=('xpath',"//span[contains(text(),'各类旅行箱 - 托运旅行箱、登机箱')]")
    backpacks_title = ('xpath', "//span[contains(text(),'各类背包 - 商务、旅行、休闲背包')]")
    crossbodies_title=('xpath',"//span[contains(text(),'托特包 - 手拎包、手袋')]")
    totes_title=('xpath',"//span[contains(text(),'斜挎包 - 休闲斜挎包')]")
    accessories_title=('xpath',"//span[contains(text(),'各类旅行配件、电子产品、钱包等')]")
    recycled_title=('xpath',"//span[contains(text(),'由可回收材料制成的环保系列')]")
    alpha3_title=('xpath',"//span[contains(text(),'全新TUMI Alpha 3系列')]")
    tumi_different=('xpath',"//h2[contains(text(),'TUMI的独特之处')]")
    j_username_error=('id',"j_username-error")
    username_error=('xpath',"//div[contains(text(),'你的用户名或密码不正确。')]")
    j_password_error=('id',"j_password-error")

class my_account_assert_element():
    my_account_title=('xpath',"//h2[contains(text(),'个人信息')]")
    store_name=('xpath',"//body/div[1]/main[1]/div[1]/div[2]/div[3]/div[1]/h2[1]")
    store_type=('xpath',"//div[contains(text(),'门店类型')]")
    diy_title=('xpath',"//p[contains(text(),'点击下方输入框激活个性化定制，激活后在输入框内输入您想要定制的字母')]")
    update_my_info=('xpath',"//a[contains(text(),'更新个人信息')]")