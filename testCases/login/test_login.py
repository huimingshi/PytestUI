# _*_ coding: utf-8 _*_ #
# @Time     :4/16/2022 2:30 PM
# @Author   :Huiming Shi
import os
import allure
import pytest
from config.project_config import CITRON_URL
from pageObjects.loginPage import LoginPage
from testDatas.login_data import public_password, group_admin_username, site_admin_username
from utils.handle_path import report_path

@allure.epic('Citron项目')
@allure.feature('登录')
class TestLogin(object):
    @allure.story('GA登录')
    @allure.title('登陆成功')
    @pytest.mark.parametrize('username,password',[(group_admin_username,public_password)])
    def test_login_GA(self,username,password,init_citron_logout):
        with allure.step('1-实例化浏览器'):
            # po = LoginPage()
            test_loginpage = init_citron_logout
        with allure.step('3-登陆操作'):
            test_loginpage.login_citron(username,password)
        with allure.step('4-断言'):
            pytest.assume(test_loginpage.get_current_url() == CITRON_URL)    # pytest-assume插件，和assert一样，只不过默认情况下assert失败后，后面的代码不会继续执行，而用assume的话，代码会继续执行
        with allure.step('5-退出driver'):
            pass


    @allure.story('SA登录')
    @allure.title('登陆成功')
    @pytest.mark.parametrize('username,password', [(site_admin_username, public_password)])
    def test_login_SA(self, username, password, exit_driver, init_citron_logout):    #  # 多个fixture的话，从后往前执行
        with allure.step('1-实例化浏览器'):
            # po = LoginPage()
            test_loginpage = init_citron_logout
        with allure.step('3-登陆操作'):
            test_loginpage.login_citron(username, password)
        with allure.step('4-断言'):
            pytest.assume(
                test_loginpage.get_current_url() == CITRON_URL)  # pytest-assume插件，和assert一样，只不过默认情况下assert失败后，后面的代码不会继续执行，而用assume的话，代码会继续执行
        with allure.step('5-退出driver'):
            pass

if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir', report_path,'--clean-alluredir'])
    os.system(f'allure serve  {report_path}')