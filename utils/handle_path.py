# _*_ coding: utf-8 _*_ #
# @Time     :4/16/2022 2:35 PM
# @Author   :Huiming Shi
import os
project_abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

report_path = os.path.join(project_abs_path,'outputs','reports','tmp')

screenshots_path = os.path.join(project_abs_path,'outputs','screenshots')

allelementyml_path = os.path.join(project_abs_path,'common','allelement.yml')

if __name__ == '__main__':
    print(allelementyml_path)