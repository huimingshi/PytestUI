# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 3:54 PM
# @Author   :Huiming Shi
from common.basePage import BasePage


class NoPage(BasePage):
    def direct_anwser_call(self):
        self.wait_click_element(self.anwser_call_button)