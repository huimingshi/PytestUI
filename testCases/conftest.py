# _*_ coding: utf-8 _*_ #
# @Time     :4/22/2022 3:30 PM
# @Author   :Huiming Shi
import os
import pytest
from pageObjects.loginPage import LoginPage

@pytest.fixture(scope='function',autouse=False)
def init_citron_logout():
    # 用例的初始化操作
    po = LoginPage()
    po.open_url()
    yield po
    # 用例的清除操作
    po.close_all_browser()
    os.system("taskkill /f /im chromedriver.exe")