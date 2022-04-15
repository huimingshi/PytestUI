# _*_ coding: utf-8 _*_ #
# @Time     :4/15/2022 4:10 PM
# @Author   :Huiming Shi

from selenium import webdriver
from config.project_config import DEF_BROWSER_TYPE, HEADLESS_FLAG, IMPLICITLY_WAIT


class CommDriver(object):
    """
    浏览器对象类
    """
    def get_driver(self,browser_type = DEF_BROWSER_TYPE,headless_flag = HEADLESS_FLAG,wait_time = IMPLICITLY_WAIT):
        """

        :param browser_type:浏览器类型
        :param headless_flag:是否无头模式
        :param wait_time:隐式等待时间
        :return:返回浏览器实例
        """
        if not headless_flag:
            if browser_type == 'Chrome':
                self.driver = webdriver.Chrome()
            elif browser_type == 'Firefox':
                self.driver = webdriver.Firefox()
            else:
                raise Exception(f'暂不支持的浏览器{browser_type}')
        else:
            if browser_type == 'Chrome':
                self.option = webdriver.ChromeOptions()
                self.option.add_argument('headless')
                self.driver = webdriver.Chrome(options=self.option)
            elif browser_type == 'Firefox':
                self.option = webdriver.ChromeOptions()
                self.option.add_argument('--headless')
                self.driver = webdriver.Firefox(options=self.option)
            else:
                raise Exception(f'暂不支持的浏览器{browser_type}')
        self.driver.maximize_window()
        self.driver.implicitly_wait(int(wait_time))
        return self.driver


if __name__ == '__main__':
    test_driver = CommDriver().get_driver()
    test_driver.quit()