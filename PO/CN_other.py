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
    crossbodies_title=('xpath',"//span[contains(text(),'托特包 - 手拎包、手袋')]")
    totes_title=('xpath',"//span[contains(text(),'斜挎包 - 休闲斜挎包')]")
    accessories_title=('xpath',"//span[contains(text(),'各类旅行配件、电子产品、钱包等')]")
    recycled_title=('xpath',"//span[contains(text(),'由可回收材料制成的环保系列')]")
    alpha3_title=('xpath',"//span[contains(text(),'全新TUMI Alpha 3系列')]")
    tumi_different=('xpath',"//h2[contains(text(),'TUMI的独特之处')]")