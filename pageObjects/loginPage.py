# _*_ coding: utf-8 _*_ #
# @Time     :4/16/2022 1:24 PM
# @Author   :Huiming Shi
import time
from config.project_config import CITRON_URL, IMPLICITLY_WAIT
from common.allElements.loginPage import *
from common.basePage import BasePage


class LoginPage(BasePage):
    """
    登录页面
    1-打开登陆页面
    2-登录系统
    """
    def open_login_page(self):
        self.open_url()

    def login_citron(self,username,password,accept = 'accept',close_bounced='close_bounced'):
        self.input_text(loc_username_input,username)
        self.wait_click_element(loc_username_input)
        self.wait_click_element(loc_next_button)
        self.driver.implicitly_wait(0.1)
        for i in range(100):
            time.sleep(1)
            ele_list = self.get_elements(loc_pwd_show)
            ele_list_next = self.get_elements(loc_next_button)
            if len(ele_list) == 1:
                self.input_text(loc_pwd_input,password)
                self.wait_click_element(loc_login_button)
                time.sleep(1)
                break
            elif len(ele_list_next) == 1:
                self.wait_click_element(loc_next_button)
            elif i == 99:
                print('password输入框还是未出现')
                raise Exception
        for i in range(100):
            time.sleep(1)
            currentPageUrl = self.get_current_url()
            print("当前页面的url是：", currentPageUrl)
            if currentPageUrl == CITRON_URL:
                break
            ele_list_login = self.get_elements(loc_login_button)
            if len(ele_list_login) == 1:
                self.wait_click_element(loc_login_button)
            elif i == 99:
                print('再次点击登录按钮未进入首页')
                raise Exception
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        if accept == 'accept':
            ele_list_disclaimer = self.get_elements(loc_accept_disclaimer)
            if len(ele_list_disclaimer) == 1:
                self.wait_click_element(loc_accept_disclaimer)
                self.driver.implicitly_wait(2)
                ele_list_disclaimer = self.get_elements(loc_accept_disclaimer)
                if len(ele_list_disclaimer) == 1:
                    self.wait_click_element(loc_accept_disclaimer)
                    self.driver.implicitly_wait(IMPLICITLY_WAIT)
        if close_bounced == 'close_bounced':
            ele_list_tutorial = self.get_elements(loc_close_tutorial)
            if len(ele_list_tutorial) == 1:
                self.wait_click_element(loc_close_tutorial)


if __name__ == '__main__':
    po = LoginPage()
    po.open_url(CITRON_URL)
    po.login_citron('Huiming.shi.helplightning+8888888888@outlook.com','*IK<8ik,8ik,')