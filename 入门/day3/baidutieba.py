#! /usr/bin/env/python
#
# coding utf-8
#
# 爬取百度贴吧的帖子
#
# jasonahven
#
'''
分析：
https://tieba.baidu.com/p/5521122026?see_lz=1&pn=1
http://  代表资源传输使用http协议
tieba.baidu.com 是百度的二级域名，指向百度贴吧的服务器。
/p/5521122026 是服务器某个资源，即这个帖子的地址定位符
see_lz和pn是该URL的两个参数，分别代表了只看楼主和帖子页码，等于1表示该条件为真
任务：
提取帖子 标题
提取帖子 回复帖数，页数
提取正文 内容
'''

import urllib.request
import urllib.parse
import re
from tool import *

class BDTB:
    def __init__(self, base_url, see_lz):
        self.base_url = base_url
        self.see_lz = "?see_lz=" + str(see_lz)

    def get_page(self, page_num):
        try:
            url = self.base_url + self.see_lz + "&pn=" + str(page_num)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
            }
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request)
        except Exception as e:
            print(e)
        if response.status != 200:
            print('url open error!')
            return None
        html = response.read().decode('utf-8')
        return html

    def get_title(self, html):
        '''
        获取标题
        '''
        pattern = re.compile(r'<h3.*?core_title_txt.*?>(.*?)</h3', re.S)
        item = re.search(pattern, html)
        if item != None:
            return item.group(1)

    def get_reply(self, html):
        '''
        获取回复总数
        '''
        pattern = re.compile(
            r'<li class="l_reply_num.*?<span.*?>(.*?)</span', re.S)
        item = re.search(pattern, html)
        if item != None:
            return item.group(1)

    def get_page_nums(self, html):
        '''
        获取总页数
        '''
        pattern = re.compile(
            r'<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        item = re.search(pattern, html)
        if item != None:
            return item.group(1)

    def getContent(self, html):
        '''
        获取每一楼层的正文
        '''
        pattern = re.compile(
            r'<div id="post_content.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, html)
        return items


if __name__ == '__main__':
    base_url = "https://tieba.baidu.com/p/5521122026"
    see_lz = input("输入是否只看楼主（0表示否，1表示是）:")
    page_num = input("输入页码（从1开始）:")
    bdtb = BDTB(base_url, see_lz)
    html = bdtb.get_page(page_num)

    title = bdtb.get_title(html)
    reply = bdtb.get_reply(html)
    page_nums = bdtb.get_page_nums(html)
    items=bdtb.getContent(html)
    tool=Tool()
    
    print(title)
    print(reply)
    print(page_nums)
    for item in items:
        print('-----------------')
        print(tool.replace(item))
