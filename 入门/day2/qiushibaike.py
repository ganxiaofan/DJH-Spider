#! /usr/bin/env/python
#
# coding utf-8
#
# 爬取糗事百科
#
# jasonahven
#

'''
分析：
不用登录，所以不用cookie
提取：作者，内容，点赞数，评论数
'''


import urllib.request
import urllib.parse
import re
from joke import *
from tool import *

def crawl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }
    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
    except Exception as e:
        print(e)
    if response.status != 200:
        print('url open error!')
        return None
    html = response.read().decode('utf-8')
    return html




def analyze(html):
    jokes = list()
    pattern = re.compile(r'h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</.*?number">(.*?)</', re.S)
    items = re.findall(pattern, html)
    tool=Tool()
    for item in items:
        author = tool.replace(item[0])
        content = tool.replace(item[1])
        like = tool.replace(item[2])
        comment = tool.replace(item[3])
        jokes.append(Joke(author, content, like, comment))
    return jokes


if __name__ == '__main__':
    page = 1
    url = 'https://www.qiushibaike.com/text/page/' + str(page)
    html = crawl(url)
    jokes = analyze(html)
    for joke in jokes:
        print('------------')
        print(joke)
