import sys,os
sys.path.append(os.getcwd())

from Page.page_in import PageIn
class TestAdress():
    # setup
    def setup_class(self):
        # 实例化统一入口类
        self.page=PageIn()
        # 调用 封装的page_login登录方法
        self.page.page_get_login().page_login_address()
        # 实例化 地址管理页面
        self.address=self.page.page_get_address()
    # teardown
    def teardown_class(self):
        self.page.driver.quit()
    # test_new_address
    # def test_new_address(self,name,phone,sheng,shi,qu,addressinfo,postcode):
    def test_new_address(self,name="张三",phone="18600000000",sheng="河南",shi="郑州",qu="二七",addressinfo="某某路梧桐街38号",postcode="472721"):
        # 点击地址管理
        self.address.page_address_manage()
        # 点击新增地址
        self.address.page_address_add_new_btn()
        # 输入收件人
        self.address.page_address_receipt_name(name)
        # 输入手机号
        self.address.page_address_add_phone(phone)
        # 点击选择区域
        self.address.page_address_province(sheng,shi,qu)
        # 输入详细地址
        self.address.page_address_detail_addr_info(addressinfo)
        # 输入邮编
        self.address.page_address_post_code(postcode)
        # 点击默认
        self.address.page_address_default()
        # 点击保存
        self.address.page_click_save()
        # 断言
        try:
            # 组装字符串 格式："张三  18610000000"
            name_phone=name+"  "+phone
            print("组装后的字符串格式：",name_phone)
            # 获取所有收件人 电话
            text_list=self.address.page_get_list_text()
            print("所有收件人电话为：",text_list)
            assert name_phone in text_list
        except:
            # 截图
            pass