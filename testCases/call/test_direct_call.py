# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 2:42 PM
# @Author   :Huiming Shi
from pageObjects.loginPage import LoginPage


class TestDirectCall(object):
    def test_direct_call(self):
        u1 = LoginPage()
        u2 = LoginPage()
        u1.open_login_page()
        u2.open_login_page()
        u1.login_citron('Huiming.shi.helplightning+EU1@outlook.com','*IK<8ik,8ik,')
        u2.login_citron('Huiming.shi.helplightning+EU1@outlook.com','*IK<8ik,8ik,')

