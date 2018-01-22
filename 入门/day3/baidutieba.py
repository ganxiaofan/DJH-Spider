#! /usr/bin/env/python
#
# coding utf-8
#
# 爬取糗事百科
#
# jasonahven
#
'''

'''

import urllib.request
import urllib.parse
import re


if __name__ == '__main__':
    page = 1
    url = 'https://www.qiushibaike.com/text/page/' + str(page)
