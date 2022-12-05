# _*_ coding: utf-8 _*_ #
# @Time     :4/15/2022 4:04 PM
# @Author   :Huiming Shi
import time
from pprint import pprint

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.common_driver import CommDriver
from config.project_config import *
import warnings
from utils.handle_path import *
from utils.handle_yml import get_yaml_data


class BasePage(object):
    """
    基类：
    1-打开浏览器
    2-打开网址
    3-定位元素
    4-点击元素
    5-输入
    """
    def __init__(self):
        self.driver = CommDriver().get_driver()
        self.locators = get_yaml_data(allelementyml_path)[self.__class__.__name__]
        for element_name,locator in self.locators.items():
            # setattr设置实例self属性element_name的值是locator
            setattr(self,element_name,locator)

    def handle_screenshot(self,action,reason):
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        self.driver.save_screenshot(f'{screenshots_path}{action}{reason}{current_time}.png')
        file_png = open(f'{screenshots_path}{action}{reason}{current_time}.png', mode='rb').read()
        allure.attach(file_png, f'{screenshots_path}{action}{reason}{current_time}.png', allure.attachment_type.PNG)
        raise Exception(f'{action}{reason}')

    def open_url(self,url=CITRON_URL,page_load_timeout = PAGE_LOAD_TIMEOUT):
        """
        打开某个url
        :param url: url地址
        :param page_load_timeout: 超时时间
        :return: None
        """
        self.driver.set_page_load_timeout(page_load_timeout)
        self.driver.get(url)

    def get_element(self,locator,action=None):
        """
        寻找元素
        加上异常保护机制，定位不到就截图
        :param locator:定位器。如(By.ID,'username')   [By.ID,'username']    ('id','username')
        :param action：元素描述信息
        :return:返回页面元素
        """
        try:
            # return self.driver.find_element(*locator)
            return WebDriverWait(self.driver,WEBDRIVERWAIT_TIMEOUT,POLL_FREQUENCY).until(EC.visibility_of_element_located(locator))
        except:
            self.handle_screenshot(action, reason='定位不到')

    def click_element(self,locator,action=None):
        """
        点击元素
        :param locator: 定位器
        :return: None
        """
        self.get_element(locator,action).click()

    def input_text_old(self, locator, text,action=None):
        """
        在元素上输入文本
        :param locator: 定位器
        :param text: 文本内容
        :return:None
        """
        # 这段代码是给这个方法添加个建议不使用的警告，但仍然可以使用
        warnings.warn('input_text_old id deprecated, please user input_text instead',DeprecationWarning)
        self.get_element(locator,action).send_keys(text)

    def input_text(self,locator,text,action=None,append = False):
        """
        在元素上输入文本
        :param locator: 定位器
        :param text: 文本内容
        :param append:书否需要清空内容后输入，默认清空
        :return:None
        """
        if not append:
            self.get_element(locator,action).clear()
            self.get_element(locator,action).send_keys(text)
        else:
            self.get_element(locator,action).send_keys(text)

    def get_elements(self,locator):
        """
        寻找元素集合
        :param locator:定位器。如(By.ID,'username')   [By.ID,'username']    ('id','username')
        :return:返回页面元素列表
        """
        return self.driver.find_elements(*locator)

    def get_current_url(self):
        """
        获取当前页面的url
        :return:
        """
        return self.driver.current_url

    def get_element_text(self,locator,action=None):
        """
        获取元素文本
        :param locator: 定位器
        :return: 返回元素文本
        """
        return self.get_element(locator,action).text

    def wait_click_element(self,locator,action=None):
        """
        采用显示等待的方式来等待元素出现后再点击
        visibility_of_element_located：判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
        :param locator:定位器
        :return:
        """
        try:
            WebDriverWait(self.driver,15,0.5).until(EC.visibility_of_element_located(locator)).click()
        except:
            self.handle_screenshot(action, reason='点击不到')

    def switch_first_window(self):
        """
        进入第一个窗口
        :param driver:
        :return:
        """
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到第一个tab页

    def open_a_new_window(self,new_url):
        """
        在原有的浏览器基础上再打开一个窗口
        :param new_url: url
        :return:
        """
        js = f"window.open('{new_url}','_blank');"
        self.driver.execute_script(js)

    def switch_window_handle(self,handle = '最后一个窗口'):
        """
        切换句柄
        :param handle:
        :return:
        """
        if handle == '最后一个窗口':
            self.driver.switch_to.window(self.driver.window_handles[-1])
        elif handle == '第一个窗口':
            self.driver.switch_to.window(self.driver.window_handles[0])

    def public_assert(self,string1,string2,condition = '=',action=None):
        try:
            if condition == '=':
                assert string1 == string2
            elif condition == 'in':
                assert string1 in string2
        except AssertionError:
            self.handle_screenshot(action, reason='断言assert失败')

    def close_all_browser(self):
        web_count = self.driver.window_handles
        for one in web_count:
            self.driver.switch_to.window(one)
            self.driver.close()

if __name__ == '__main__':
    # driver = BasePage()
    # driver.open_url(CITRON_URL)
    # driver.click_element(('xpath','//input[@autocomplete="username"]'))
    # driver.input_text_old(('xpath', '//input[@autocomplete="username"]'), 'Huiming.shi.helplightning+8888888888@outlook.com')
    # driver.input_text(('xpath', '//input[@autocomplete="username"]'), 'Huiming.shi.helplightning+8888888888@outlook.com')
    # pprint(driver.locators)
    class MainPage(BasePage):
        pass

    mp = MainPage()
    # pprint(mp.locators)
    # pprint(mp.loc_contacts_page)
    mp.open_a_new_window('http://www.baidu.com')