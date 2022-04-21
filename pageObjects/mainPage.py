# _*_ coding: utf-8 _*_ #
# @Time     :4/20/2022 6:07 PM
# @Author   :Huiming Shi
from common.basePage import BasePage
from config.project_config import IMPLICITLY_WAIT


class MainPage(BasePage):
    def switch_tree(self,if_click_tree = None,witch_tree = 2):
        if if_click_tree:
            if int(witch_tree) == 1:
                self.wait_click_element(self.loc_first_tree)
            elif int(witch_tree) == 2:
                self.wait_click_element(self.loc_second_tree)
            else:
                self.wait_click_element(self.loc_third_tree)

    def go_to_contacts(self,if_click_tree = None,witch_tree = 2):
        self.switch_tree(if_click_tree,witch_tree)
        self.wait_click_element(self.loc_contacts_page)