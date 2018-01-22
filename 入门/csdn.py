#! /usr/bin/env/python
#
# coding utf-8
#
# jasonahven
#
#
# refer:http://blog.csdn.net/yanggd1987/article/details/52127436

import urllib.request
import urllib.parse as parse
import http.cookiejar as cookiejar
from bs4 import BeautifulSoup

if __name__ == '__main__':
    loginurl = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

    filename = 'cookie_csdn.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(filename)
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib.request.build_opener(handler)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'),
                              ('Referer', 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'), ('Host', 'passport.csdn.net')]

    # 登陆前准备：获取lt和exection
    response=opener.open(loginurl)
    soup=BeautifulSoup(response.read(), "lxml")
    for input in soup.form.find_all("input"):
        if input.get("name") == "lt":
            lt=input.get("value")
        if input.get("name") == "execution":
            execution=input.get("value")

    values={
        "username": "username",
        "password": "password",
        "lt": lt,
        "execution": execution,
        "_eventId": "submit"
    }
    postdata = urllib.parse.urlencode(values).encode('utf-8')
    
    # 模拟登录,保存cookie到cookie.txt中
    response = opener.open(loginurl, postdata)
    print(response.status)

    cookie.save(ignore_discard=True, ignore_expires=True)
    
    # 登陆后我们随意跳转到博客
    url = "http://blog.csdn.net/XXXXXXXXX"
    response = opener.open(url)
    print(response.status)