# _*_ coding: utf-8 _*_ #
# @Time     :4/21/2022 5:21 PM
# @Author   :Huiming Shi

import time
def get_random_str():
    get_random = time.time() * 1000000
    random_str = str(get_random).split('.')[0]
    return random_str

if __name__ == '__main__':
    print(get_random_str())