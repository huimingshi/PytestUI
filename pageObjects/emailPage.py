# _*_ coding: utf-8 _*_ #
# @Time     :4/22/2022 9:54 AM
# @Author   :Huiming Shi
import time
import pytest
from common.basePage import BasePage
from testDatas.login_data import public_password
from utils.handle_email import set_your_password_email


class EmailPage(BasePage):
    def set_your_password(self):
        """
        设置密码
        :return:
        """
        time.sleep(20)
        # 从outlook邮箱获取邮件
        email_link = set_your_password_email()
        # 打开这个邮件的设置密码链接
        self.open_a_new_window(email_link)
        # 切换到第二个句柄，就是设置密码的窗口
        self.switch_window_handle()
        # 输入密码
        self.wait_click_element(self.set_password)
        self.input_text(self.set_password,public_password)
        # 确认密码
        self.input_text(self.confirm_set_password, public_password)
        # 点击确定
        self.wait_click_element(self.set_password_button)
        # 断言
        pytest.assume(len(self.get_elements(self.set_password_success)) == 1)
        # 切换到第一个句柄，就是原始窗口
        self.switch_window_handle(handle='第一个窗口')