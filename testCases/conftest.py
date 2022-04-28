# _*_ coding: utf-8 _*_ #
# @Time     :4/22/2022 3:30 PM
# @Author   :Huiming Shi
import os
import pytest
from pageObjects.loginPage import LoginPage
from testDatas.login_data import site_admin_username, public_password


@pytest.fixture(scope='function',autouse=False)
def init_citron_logout():
    # 用例的初始化操作
    test_loginpage = LoginPage()
    test_loginpage.open_url()
    yield test_loginpage
    # 用例的清除操作
    test_loginpage.close_all_browser()
    os.system("taskkill /f /im chromedriver.exe")