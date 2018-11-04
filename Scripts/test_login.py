import os,sys
sys.path.append(os.getcwd())
from Base.read_yaml import ReadYaml
import allure
import pytest
from Page.Page_in import PageIn


def get_data():
    #     自定义空列表
    arrs = []
    # 获取出的结果为列表，列表内单个元素值为字典 data.values
    for data in ReadYaml("login_data.yml").read_yaml().values():
        arrs.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
    return arrs


class TestLogin():
    def setup_class(self):

        self.page = PageIn()
        self.login = self.page.page_get_login()

        # 点击我
        self.login.page_click_me()
        # 点击已有账号去登录
        self.login.page_click_me_ok_link()

    def teardown_class(self):
        # 关闭driver 驱动对象
        self.login.driver.quit()

    @pytest.mark.parametrize("username,password,expect_result,expect_toast",get_data())
    def test_login(self, username, password, expect_result,expect_toast):
        if expect_result :

            # 输入账号
            self.login.page_input_username(username)
             # 输入密码
            self.login.page_input_pwd(password)
             # 点击登录
            self.login.page_click_login_btn()
            # 获取昵称
            nickname = self.login.page_get_nickname()
            try:
                assert expect_result in nickname
                # 设置
                self.login.page_click_setting()
                # 滑动
                self.login.page_drag_ang_drop()
                # 点击退出
                self.login.page_click_exit()
                # 确认退出
                self.login.page_click_exit_ok()

                # 点击我
                self.login.page_click_me()
                # 点击已有账号去登录
                self.login.page_click_me_ok_link()

            except:
                # 截图
                self.login.base_get_screenshot()
                # 失败图片写入报告
                with open("./Image/faild.png", "rb")as f:
                    allure.attach("失败原因请查看附加图", f.read(), allure.attach_type.PNG)
                # 抛异常
                raise
        else:
            try:
                # 输入账号
                self.login.page_input_username(username)
                # 输入密码
                self.login.page_input_pwd(password)
                # 点击登录
                self.login.page_click_login_btn()
                #expect_toast
                assert expect_toast in self.login.base_get_toast(expect_toast)

            except:
                # 截图
                self.login.base_get_screenshot()
                # 失败图片写入报告
                with open("./Image/faild.png", "rb")as f:
                    allure.attach("失败原因请查看附加图", f.read(), allure.attach_type.PNG)
                # 抛异常
                raise



