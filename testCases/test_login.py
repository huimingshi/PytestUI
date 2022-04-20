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


class TestLogin(object):
    @pytest.mark.parametrize('username,password',[(username_888,password_888)])
    def test_login(self,username,password):
        po = LoginPage()
        po.open_url(CITRON_URL)
        po.login_citron(username,password)
        assert po.get_current_url() == CITRON_URL


if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir', report_path,'--clean-alluredir'])
    os.system(f'allure serve  {report_path}')