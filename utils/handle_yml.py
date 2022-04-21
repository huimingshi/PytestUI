# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 1:17 PM
# @Author   :Huiming Shi
from pprint import pprint

import yaml

from utils.handle_path import allelementyml_path


def get_yaml_data(fileDir):
    """
    获取yaml文件的内容
    :param fileDir:yaml的文件路径
    :return:返回yaml的文件内容
    """
    with open(fileDir,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())

if __name__ == '__main__':
    res = get_yaml_data(allelementyml_path)
    pprint(res)