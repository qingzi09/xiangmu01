import Page
from Base.base import Base
class PageAddress(Base):
    # 点击地址管理
    def page_address_manage(self):
        self.base_click(Page.address_manage)
    # 点击新增地址
    def page_address_add_new_btn(self):
        self.base_click(Page.address_add_new_btn)
    # 输入收件人
    def page_address_receipt_name(self,name):
        self.base_input(Page.address_receipt_name,name)
    # 输入手机号
    def page_address_add_phone(self,phone):
        self.base_input(Page.address_add_phone,phone)
    # 选择区域
    def page_address_province(self,sheng,shi,qu):
        # 点击选择区域
        self.base_click(Page.address_province)
        # 点击 省
        self.page_click_sheng(sheng)
        # 点击 市
        self.page_click_shi(shi)
        # 点击 区
        self.page_click_qu(qu)
    # 输入详细地址
    def page_address_detail_addr_info(self,addressinfo):
        self.base_input(Page.address_detail_addr_info,addressinfo)
    # 省
    def page_click_sheng(self,sheng):
        self.base_xpath_text_click(sheng)
    """
        注意：
            1. 省、市、区、保存、可以不在此地方封装，在执行脚本时直接调用
    """
    # 市
    def page_click_shi(self,shi):
        self.base_xpath_text_click(shi)
    # 区
    def page_click_qu(self,qu):
        self.base_xpath_text_click(qu)
    # 输入邮编
    def page_address_post_code(self,postcode):
        self.base_input(Page.address_post_code,postcode)
    # 点击默认地址
    def page_address_default(self):
        self.base_click(Page.address_default)
    # 点击保存
    def page_click_save(self):
        self.base_xpath_text_click("保存")
    # 返回所有 收件人 电话
    def page_get_list_text(self):
        return self.base_get_list_text(Page.address_name_phone)









    pass