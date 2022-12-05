# _*_ coding: utf-8 _*_ #
# @Time     :12/5/2022 11:03 AM
# @Author   :Huiming Shi
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.mainPage import MainPage


@pytest.fixture(scope='function',autouse=False)
def init_citron_logout():
    test_loginpage = LoginPage()
    test_loginpage.open_url()
    yield test_loginpage
    # 用例的清除操作
    # test_loginpage.close_all_browser()
    MainPage().logout()

@pytest.fixture(scope='function',autouse=False)
def exit_driver():
    test_loginpage = LoginPage()
    # yield test_loginpage
    yield
    # 用例的清除操作
    test_loginpage.close_all_browser()