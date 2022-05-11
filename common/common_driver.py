# _*_ coding: utf-8 _*_ #
# @Time     :4/15/2022 4:10 PM
# @Author   :Huiming Shi

from selenium import webdriver
from config.project_config import DEF_BROWSER_TYPE, HEADLESS_FLAG, IMPLICITLY_WAIT

class Single(object):
    # 一个下划线'_'开头的是建议性的私有变量
    # 两个下划线'__'开头的才是私有变量
    _instance = None    # 类变量，存储实例
    def __new__(cls, *args, **kwargs):     # 类方法但没有classmethod装饰器
        if cls._instance is None:    # 如果没有实例化过
            cls._instance = super().__new__(cls)     # new一下
        return cls._instance    # 返回实例对象

class CommDriver(Single):
    """
    浏览器对象类
    """

    driver = None    # 用来控制只产生一个浏览器的
    def get_driver(self,browser_type = DEF_BROWSER_TYPE,headless_flag = HEADLESS_FLAG,wait_time = IMPLICITLY_WAIT):
        """

        :param browser_type:浏览器类型
        :param headless_flag:是否无头模式
        :param wait_time:隐式等待时间
        :return:返回浏览器实例
        """
        if self.driver is None:   # 配合上面，如果产生过就不继续产生（执行代码），没有产生的话就产生一个浏览器对象
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