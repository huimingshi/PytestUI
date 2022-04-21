# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 3:58 PM
# @Author   :Huiming Shi
import time
from common.basePage import BasePage


class InCallPage(BasePage):
    def exit_call(self,call_time = 20):
        # 维持通话20s
        time.sleep(int(call_time))
        # User exit call
        self.wait_click_element(self.end_call_button)
        self.wait_click_element(self.exit_call_yes)