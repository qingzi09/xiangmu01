import Page
import allure
from Base.base import Base


class PageLogin(Base):
    # 点击我
    def page_click_me(self):
        self.base_click(Page.login_me)

    # 点击已有账号去登录

    def page_click_me_ok_link(self):
        self.base_click(Page.login_name_ok_link)

    # 输入账号
    @allure.step("输入账号")
    def page_input_username(self, username):
        self.base_input(Page.login_username, username)

    # 输入密码
    @allure.step("输入密码")
    def page_input_pwd(self, password):
        self.base_input(Page.login_password, password)
    # 点击登录
    @allure.step("点击登录")
    def page_click_login_btn(self):
        self.base_click(Page.login_btn)

    #  获取昵称 断言 base_get_text

    def page_get_nickname(self):
        return self.base_get_text(Page.login_nickname)

    # 点击设置
    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click(Page.login_setting)

    # 滑动 消息推送-->修改密码
    @allure.step("滑动 消息推送-->修改密码")
    def page_drag_ang_drop(self):
        el1 = self.base_find_element(Page.login_msg_send)
        el2 = self.base_find_element(Page.login_modify_pwd)
        self.base_drag_and_drop(el1,el2)

    # 点击退出按钮
    @allure.step("点击退出按钮")
    def page_click_exit(self):
        self.base_click(Page.login_logout)

    # 确认退出
    @allure.step("确认退出")
    def page_click_exit_ok(self):
        self.base_click(Page.login_logout_ok)

#     封建登录操作 给地址管理使用
    def page_login_address(self):
        # 点击我
        self.page_click_me()
        # 点击已有账号去登录
        self.page_click_me_ok_link()
        # 输入用户名
        self.page_input_username("18610453007")
        #输入密码
        self.page_input_pwd("123456")
        # 点击登录
        self.page_click_login_btn()
        # 点击设置
        self.page_click_setting()