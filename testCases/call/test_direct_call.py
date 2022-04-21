# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 2:42 PM
# @Author   :Huiming Shi
import pytest
import allure
from pageObjects.contactsPage import ContactsPage
from pageObjects.incallPage import InCallPage
from pageObjects.loginPage import LoginPage
from pageObjects.noPage import NoPage
from utils.handle_path import report_path

@allure.epic('Citron项目')
@allure.feature('通话功能')
class TestDirectCall(object):
    @allure.title('用户直接通话')
    def test_direct_call(self):
        test_loginpage_1 = LoginPage()
        test_loginpage_2 = LoginPage()
        test_loginpage_1.open_login_page()
        test_loginpage_2.open_login_page()
        test_loginpage_1.login_citron('Huiming.shi.helplightning+EU1@outlook.com','*IK<8ik,8ik,')
        test_loginpage_2.login_citron('Huiming.shi.helplightning+EU1@outlook.com','*IK<8ik,8ik,')
        test_contactspage_1 = ContactsPage()
        test_contactspage_1.contacts_search_user('Huiming.shi.helplightning+EU1@outlook.com')
        test_nopage_2 = NoPage()
        test_nopage_2.direct_anwser_call()
        test_incallpage_1 = InCallPage()
        test_incallpage_1.exit_call()


if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir', report_path,'--clean-alluredir'])
    os.system(f'allure serve  {report_path}')