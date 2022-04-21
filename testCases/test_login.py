# _*_ coding: utf-8 _*_ #
# @Time     :4/16/2022 2:30 PM
# @Author   :Huiming Shi
import os
import allure
import pytest
from config.project_config import CITRON_URL
from pageObjects.loginPage import LoginPage
from testDatas.login_data import username_888,password_888
from utils.handle_path import report_path

@allure.epic('Citron项目')
@allure.feature('登录')
class TestLogin(object):
    @allure.title('登陆成功')
    @pytest.mark.parametrize('username,password',[(username_888,password_888)])
    def test_login(self,username,password):
        with allure.step('1-实例化浏览器'):
            po = LoginPage()
        with allure.step('2-打开登录页面'):
            po.open_url(CITRON_URL)
        with allure.step('3-登陆操作'):
            po.login_citron(username,password)
        with allure.step('4-断言'):
            pytest.assume(po.get_current_url() == CITRON_URL)    # pytest-assume插件，和assert一样，只不过默认情况下assert失败后，后面的代码不会继续执行，而用assume的话，代码会继续执行


if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir', report_path,'--clean-alluredir'])
    os.system(f'allure serve  {report_path}')