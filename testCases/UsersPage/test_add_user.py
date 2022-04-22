# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 6:43 PM
# @Author   :Huiming Shi
import os
import pytest
import allure
from pageObjects.emailPage import EmailPage
from pageObjects.loginPage import LoginPage
from pageObjects.mainPage import MainPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.usersPage import UsersPage
from testDatas.login_data import site_admin_username,public_password
from utils.handle_path import report_path


@allure.epic('Citron项目')
@allure.feature('Site Admin的操作')
class Test_add_user(object):
    @allure.story('Add User')
    @allure.title('新增normal user')
    def test_add_user(self,init_citron_logout):
        with allure.step('1-登录操作'):
            # test_loginpage = LoginPage()
            # test_loginpage.open_login_page()
            init_citron_logout.login_citron(site_admin_username, public_password)
        with allure.step('2-切换到Users页面'):
            test_mainpage = MainPage()
            test_mainpage.switch_tree(if_click_tree = 'yes',witch_tree = 2)
            test_mainpage.go_to_users()
        with allure.step('3-add user的操作，内部已加断言'):
            test_userspage = UsersPage()
            test_userspage.click_add_user_button()
            email,name = test_userspage.create_user(groups = 'auto_default_group')
        with allure.step('4-从outlook邮箱获取邮件，并打开这个邮件的设置密码链接'):
            test_emailpage = EmailPage()
            test_emailpage.set_your_password()
        with allure.step('5-Active Users页面查询这个新建的user'):
            test_userspage.search_active_user(email)
        with allure.step('6-退出登录'):
            test_myaccountpage = MyAccountPage()
            test_myaccountpage.click_my_account()
            test_myaccountpage.logout_citron()
        with allure.step('7-新建的user进行登录'):
            init_citron_logout.login_citron(email, public_password)

if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir', report_path,'--clean-alluredir'])
    os.system(f'allure serve  {report_path}')