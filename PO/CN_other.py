# @Author ：黄贝尔
# @Time ：2021/2/7__14:23
# #coding:utf-8
class assert_element():
    vip_Privilege=('xpath',"//strong[contains(text(),'会员专属礼遇')]")
    wechat_text=('xpath','//header/div[3]/div[2]/a[2]/div[1]/div[2]/p[1]')
    store_type=('xpath',"//div[contains(text(),'门店类型')]")
    login_text=('xpath',"//span[contains(text(),'登录您的TUMI.CN账号')]")
    no_search=('xpath',"//div[contains(text(),'对不起，没有搜索结果')]")
    have_search=('xpath',"//div[contains(text(),'搜索结果')]")
    luggage_title=('xpath',"//span[contains(text(),'各类旅行箱 - 托运旅行箱、登机箱')]")
    backpacks_title = ('xpath', "//span[contains(text(),'各类背包 - 商务、旅行、休闲背包')]")