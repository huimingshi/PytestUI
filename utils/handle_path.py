# _*_ coding: utf-8 _*_ #
# @Time     :4/16/2022 2:35 PM
# @Author   :Huiming Shi
import os
# 项目的绝对路径
project_abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# report的绝对路径
report_path = os.path.join(project_abs_path,'outputs','reports','tmp')
# 截图的绝对路径
screenshots_path = os.path.join(project_abs_path,'outputs','screenshots','截图--')
# 存放元素定位的yml文件的绝对路径
allelementyml_path = os.path.join(project_abs_path,'common','allelement.yml')

if __name__ == '__main__':
    print(screenshots_path)