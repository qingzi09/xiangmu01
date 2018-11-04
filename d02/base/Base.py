import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver

    # 查找元素方法  封装--》此方法给click、input等方法使用
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击方法封装
    def base_click(self,loc):
        self.base_find_element(loc).click()

    # 输入方法封装
    def base_input(self,loc,text):
        el=self.base_find_element(loc)
        el.clear()
        el.send_keys(text)
    # 截图方法封装
    def base_get_screenshot(self):
        img_path = os.getcwd()+os.sep+"image"+os.sep+"faild.pnd"
        self.driver.get_screenshot_as_file(img_path)


    # 获取toast 封装
    def base_get_toast(self,loc,message):
        msg = By.XPATH,"//*[contains(@text,'"+message+"')]"

        return self.base_find_element(msg,poll=0.1).text

    # 获取文本内容
    def base_get_text(self,loc):
        return self.base_find_element(loc).text

    # 滑动
    def base_drag_and_drop(self,el1,el2):

        self.driver.base_drag_and_drop(el1,el2)