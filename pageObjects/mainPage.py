# _*_ coding: utf-8 _*_ #
# @Time     :4/20/2022 6:07 PM
# @Author   :Huiming Shi
import time
from common.basePage import BasePage
from config.project_config import IMPLICITLY_WAIT


class MainPage(BasePage):
    def switch_tree(self,if_click_tree = None,witch_tree = 2):
        if if_click_tree:
            if int(witch_tree) == 1:
                self.wait_click_element(self.loc_first_tree,'第一目录树')
            elif int(witch_tree) == 2:
                self.wait_click_element(self.loc_second_tree,'第二目录树')
            else:
                self.wait_click_element(self.loc_third_tree,'第三目录树')
        time.sleep(3)

    def go_to_contacts(self):
        self.wait_click_element(self.loc_contacts_page,'Contacts页面')

    def go_to_users(self):
        self.wait_click_element(self.loc_users_page,'Users页面')