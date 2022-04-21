# _*_ coding: utf-8 _*_ #
# @Time     :4/20/2022 5:20 PM
# @Author   :Huiming Shi
from common.basePage import BasePage
from config.project_config import IMPLICITLY_WAIT

class ContactsPage(BasePage):
    def contacts_search_user(self,username):
        self.driver.implicitly_wait(1)
        for i in range(20):
            ele_list = self.get_elements(self.loc_contacts_text)
            ele_list_call = self.get_elements(self.loc_contacts_call)
            if len(ele_list_call) == 1 and len(ele_list) == 1:
                self.driver.implicitly_wait(IMPLICITLY_WAIT)
                break
        self.wait_click_element(self.loc_contacts_search)
        self.input_text(self.loc_contacts_search,username)
        self.wait_click_element(self.loc_contacts_call)