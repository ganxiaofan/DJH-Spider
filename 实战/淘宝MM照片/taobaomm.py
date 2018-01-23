#! /usr/bin/env/python
#
# coding utf-8
#
# 爬取淘宝MM
#
# jasonahven
#

'''
分析：


任务目标：
- 爬取
1.MMID
2.姓名
3.体重
4.城市
5.职业
6.风格
7.头像
8.写真
- 把每一个MM的写真图片按照文件夹保存到本地
- 把信息保存在数据库中
'''


import urllib.request
import re
from tool import Tool
from mm import MM
import json
import zlib
from save import *


def crawl_info(url):
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

    # bytes = response.read()
    # decompressed_data = zlib.decompress(bytes, 16 + zlib.MAX_WBITS)
    # html = decompressed_data.decode('utf-8')
    html = response.read().decode('gbk')
    response.close()

    pattern = re.compile(
        r'<div.*?mm-p-base-info.*?职.*?业.*?<span>(.*?)</', re.S)
    item = re.search(pattern, html)

    occupation, style = 'None', 'None'
    if item != None:
        occupation = item.group(1)

    pattern = re.compile(
        r'<div.*?mm-p-base-info.*?风.*?格.*?<span>(.*?)</', re.S)
    item = re.search(pattern, html)
    if item != None:
        style = item.group(1)

    return occupation, style


def load_json(file):
    load_dict = {}
    # 加载json文件
    with open(file, 'r', encoding='utf-8') as f:
        load_dict = json.load(f)
    return load_dict


def analyze_json(dict):
    # 分析json文件
    mms = []
    items = dict['data']['searchDOList']
    for item in items:
        userId = item['userId']
        realName = item['realName']
        weight = item['weight']
        city = item['city']
        avatarUrl = item['avatarUrl']
        cardUrl = item['cardUrl']

        url = "https://mm.taobao.com/self/info/model_info_show.htm?user_id=" + \
            str(userId)

        # 从个人主页爬取信息
        occupation, style = crawl_info(url)

        mms.append(MM(str(userId), str(realName), str(weight), str(city),
                      str(occupation), str(style), str(avatarUrl), str(cardUrl)))

    return mms


if __name__ == "__main__":
    json_file = '实战\\淘宝MM照片\\tstar_model.json'
    # 加载json数据到dict
    load_dict = load_json(json_file)
    # 解析数据得到mms
    mms = analyze_json(load_dict)
    # 保存mms到数据库和文件
    user = 'root'
    pwd = 'root'
    db = 'taobao'
    table = 'mm'
    save_info(user, pwd, db, table, mms)
    save_photos(mms)
