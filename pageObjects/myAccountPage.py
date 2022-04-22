# _*_ coding: utf-8 _*_ #
# @Time     :4/22/2022 1:57 PM
# @Author   :Huiming Shi
from common.basePage import BasePage


class MyAccountPage(BasePage):
    def click_my_account(self):
        # 点击右上角的我的账号
        self.wait_click_element(self.my_account_button)

    def logout_citron(self):
        # 点击logout退出系统
        self.wait_click_element(self.logout_button)