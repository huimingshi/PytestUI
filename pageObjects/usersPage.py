# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 5:09 PM
# @Author   :Huiming Shi
import pytest
from common.basePage import BasePage
from utils.handle_random_str import get_random_str

class UsersPage(BasePage):
    def click_add_user_button(self):
        # 点击ADD USER按钮
        self.wait_click_element(self.add_user_button,'ADD_USER按钮')

    def create_user(self, licence_type = 'Expert', role = 'User', choose_group = True, groups = None):
        # 获取随机的email和name
        email = f'Huiming.shi.helplightning+{get_random_str()}@outlook.com'
        name = f'Huiming.shi.helplightning+{get_random_str()}'
        # 等待email输入框可见
        self.wait_click_element(self.email_input,'email输入框')
        # 输入email
        self.input_text(self.email_input,email,'email输入框')
        # 输入name
        self.input_text(self.name_input,name,'name输入框')
        # 输入title
        self.input_text(self.title_input, name,'title输入框')
        # 输入location
        self.input_text(self.location_input, name,'location输入框')
        # 选择License Type
        if licence_type == 'Team':
            self.click_element(self.choose_license_type,'License_type选择器')
            self.wait_click_element(self.team_license_type,'Team_Type选择')
        # 选择Role
        if role == 'Group Admin':
            self.click_element(self.select_role,'Role选择器')
            self.wait_click_element(self.ga_role,'Group_Admin选择')
        elif role == 'Workspace Admin':
            self.click_element(self.select_role,'Role选择器')
            self.wait_click_element(self.wa_role,'Workspace_Admin选择')
        # 选择Groups
        if choose_group:
            self.click_element(self.groups_input,'Groups选择器')
            self.select_witch_group[-1] = self.select_witch_group[-1].format(groups)
            self.wait_click_element(self.select_witch_group,'具体的group')
        # 点击ADD按钮
        self.click_element(self.add_button,'ADD按钮')
        # 断言
        pytest.assume(len(self.get_elements(self.prompt_information)) == 1)