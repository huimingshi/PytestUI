# _*_ coding: utf-8 _*_ #
# @Time     :4/15/2022 2:08 PM
# @Author   :Huiming Shi


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
"""
元素定位的多种实现方法
"""
driver.find_element_by_id('kw')
# driver.find_element('id','kw').send_keys('111')
# driver.find_element(By.ID,'kw').send_keys('111')    # 需要导入By这个类
id_ele_locator = ('id','kw')
driver.find_element(*id_ele_locator).send_keys('111')    # *()是把元组进行解包成多个字符串