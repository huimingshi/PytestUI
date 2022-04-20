# _*_ coding: utf-8 _*_ #
# @Time     :4/15/2022 4:04 PM
# @Author   :Huiming Shi
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.common_driver import CommDriver
from config.project_config import CITRON_URL
import warnings

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

    def open_url(self,url=CITRON_URL):
        """
        打开某个url
        :param url: url地址
        :return: None
        """
        self.driver.get(url)

    def get_element(self,locator):
        """
        寻找元素
        :param locator:定位器。如(By.ID,'username')   [By.ID,'username']    ('id','username')
        :return:返回页面元素
        """
        return self.driver.find_element(*locator)

    def click_element(self,locator):
        """
        点击元素
        :param locator: 定位器
        :return: None
        """
        self.get_element(locator).click()

    def input_text_old(self, locator, text):
        """
        在元素上输入文本
        :param locator: 定位器
        :param text: 文本内容
        :return:None
        """
        # 这段代码是给这个方法添加个建议不使用的警告，但仍然可以使用
        warnings.warn('input_text_old id deprecated, please user input_text instead',DeprecationWarning)
        self.get_element(locator).send_keys(text)

    def input_text(self,locator,text,append = False):
        """
        在元素上输入文本
        :param locator: 定位器
        :param text: 文本内容
        :param append:书否需要清空内容后输入，默认清空
        :return:None
        """
        if not append:
            self.get_element(locator).clear()
            self.get_element(locator).send_keys(text)
        else:
            self.get_element(locator).send_keys(text)

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

    def get_element_text(self,locator):
        """
        获取元素文本
        :param locator: 定位器
        :return: 返回元素文本
        """
        return self.get_element(locator).text

    def wait_click_element(self,locator):
        """
        采用显示等待的方式来等待元素出现后再点击
        visibility_of_element_located：判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
        :param locator:定位器
        :return:
        """
        WebDriverWait(self.driver,15,0.5).until(EC.visibility_of_element_located(locator)).click()

if __name__ == '__main__':
    driver = BasePage()
    driver.open_url(CITRON_URL)
    driver.click_element(('xpath','//input[@autocomplete="username"]'))
    # driver.input_text_old(('xpath', '//input[@autocomplete="username"]'), 'Huiming.shi.helplightning+8888888888@outlook.com')
    driver.input_text(('xpath', '//input[@autocomplete="username"]'), 'Huiming.shi.helplightning+8888888888@outlook.com')