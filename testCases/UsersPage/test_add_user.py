# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 6:43 PM
# @Author   :Huiming Shi
import os
import pytest
import allure
from pageObjects.loginPage import LoginPage
from pageObjects.mainPage import MainPage
from pageObjects.usersPage import UsersPage
from utils.handle_path import report_path


@allure.epic('Citron项目')
@allure.feature('Site Admin的操作')
class Test_add_user(object):
    @allure.story('Add User')
    @allure.title('新增normal user')
    def test_add_user(self):
        with allure.step('1-登录操作'):
            test_loginpage = LoginPage()
            test_loginpage.open_login_page()
            test_loginpage.login_citron('huiming.shi@helplightning.com', '*IK<8ik,8ik,')
        with allure.step('2-切换到Users页面'):
            test_mainpage = MainPage()
            test_mainpage.switch_tree(if_click_tree = 'yes',witch_tree = 2)
            test_mainpage.go_to_users()
        with allure.step('3-add user的操作，内部已加断言'):
            test_userspage = UsersPage()
            test_userspage.click_add_user_button()
            test_userspage.create_user(groups = 'auto_default_group')



if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir', report_path,'--clean-alluredir'])
    os.system(f'allure serve  {report_path}')