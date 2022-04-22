# _*_ coding: utf-8 _*_ #
# @Time     :4/16/2022 1:24 PM
# @Author   :Huiming Shi
import time
from config.project_config import CITRON_URL, IMPLICITLY_WAIT
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
        # 输入username
        self.wait_click_element(self.loc_username_input,'username输入框')
        self.input_text(self.loc_username_input, username, 'username输入框')
        # 点击NEXT按钮
        self.wait_click_element(self.loc_next_button, 'NEXT按钮')
        self.driver.implicitly_wait(0.1)
        # 检查是否出现password输入框
        for i in range(100):
            time.sleep(1)
            ele_list = self.get_elements(self.loc_pwd_show)
            ele_list_next = self.get_elements(self.loc_next_button)
            # 如果出现password输入框
            if len(ele_list) == 1:
                # 输入password
                self.input_text(self.loc_pwd_input,password,'password输入框')
                # 点击LOGIN按钮
                self.wait_click_element(self.loc_login_button,'LOGIN按钮')
                time.sleep(1)
                break
            # 如果NEXT按钮还在
            elif len(ele_list_next) == 1:
                # 就再点击NEXT按钮
                self.wait_click_element(self.loc_next_button, 'NEXT按钮')
            elif i == 99:
                print('password输入框还是未出现')
                raise Exception
        # 检查是否登陆成功
        for i in range(100):
            time.sleep(1)
            currentPageUrl = self.get_current_url()
            print("当前页面的url是：", currentPageUrl)
            if currentPageUrl == CITRON_URL:
                break
            ele_list_login = self.get_elements(self.loc_login_button)
            # 如果LOGIN按钮还在
            if len(ele_list_login) == 1:
                # 再点击LOGIN按钮
                self.wait_click_element(self.loc_login_button,'LOGIN按钮')
            elif i == 99:
                print('再次点击登录按钮未进入首页')
                raise Exception
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        # accept Disclaimer
        if accept == 'accept':
            ele_list_disclaimer = self.get_elements(self.loc_accept_disclaimer)
            if len(ele_list_disclaimer) == 1:
                self.wait_click_element(self.loc_accept_disclaimer,'ACCEPT_DISCLAIMER按钮')
                self.driver.implicitly_wait(2)
                # 担心会出现两个Disclaimer
                ele_list_disclaimer = self.get_elements(self.loc_accept_disclaimer)
                if len(ele_list_disclaimer) == 1:
                    self.wait_click_element(self.loc_accept_disclaimer,'ACCEPT_DISCLAIMER按钮')
                    self.driver.implicitly_wait(IMPLICITLY_WAIT)
        # 关闭Tutorial
        if close_bounced == 'close_bounced':
            ele_list_tutorial = self.get_elements(self.loc_close_tutorial)
            if len(ele_list_tutorial) == 1:
                self.wait_click_element(self.loc_close_tutorial,'close_tutorial按钮')


if __name__ == '__main__':
    po = LoginPage()
    po.open_url(CITRON_URL)
    po.login_citron('Huiming.shi.helplightning+8888888888@outlook.com','*IK<8ik,8ik,')