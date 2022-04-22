# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 5:09 PM
# @Author   :Huiming Shi
import time
from config.project_config import IMPLICITLY_WAIT
import pytest
from common.basePage import BasePage
from utils.handle_random_str import get_random_str

class UsersPage(BasePage):
    def click_add_user_button(self):
        """
        点击ADD USER按钮
        :return:
        """
        self.wait_click_element(self.add_user_button,'ADD_USER按钮')

    def create_user(self, licence_type = 'Expert', role = 'User', choose_group = True, groups = None):
        """
        新建user
        :param licence_type:
        :param role:
        :param choose_group:
        :param groups:
        :return:
        """
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
        # 断言出现创建成功的提示信息
        self.public_assert(len(self.get_elements(self.prompt_information)),1,'出现创建成功的提示信息')
        # 返回email和username
        return email,name

    def search_active_user(self,user_email):
        """
        Active Users标签页查询user
        :param user_email:
        :return:
        """
        # Active Users页面查询用户
        self.input_text(self.active_user_search,text=user_email,action='Active_Users查询框')
        self.driver.implicitly_wait(1)
        for i in range(30):
            ele_count = self.get_elements(self.user_list_count)
            if len(ele_count) == 1:
                break
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        # 断言查询出来就一条数据
        self.public_assert(len(self.get_elements(self.user_list_count)),1,'查询出来就一条数据')
        # 断言这条数据就是刚新增的user
        self.public_assert(self.get_element_text(self.first_user_email,'第一个user的email'), user_email,'这条数据就是刚新增的user')