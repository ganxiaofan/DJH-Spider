#! /usr/bin/env/python
#
# coding utf-8
#
# jasonahven
#


import urllib.request
import urllib.parse
import http.cookiejar as cookiejar


def save_cookies_to_file(file):
    #声明一个MozillaCookieJar对象实例来保存cookies
    cookies=cookiejar.MozillaCookieJar(file)
    cookies.save(ignore_discard=True,ignore_expires=True)

def read_cookies_from_file(file):
    cookies=cookiejar.MozillaCookieJar()
    cookies.load(file,ignore_expires=True,ignore_discard=True)
    return cookies


if __name__ == '__main__':
    url = 'http://www.baidu.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }

    request=urllib.request.Request(url,headers=headers)

    #使用cookie保存到变量cookies
    #声明一个CookieJar对象实例来保存cookie
    cookies = cookiejar.CookieJar()
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler=urllib.request.HTTPCookieProcessor(cookies)
    #通过handler来构建opener
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)

    print(cookies)
    
    if response.getcode() != 200:
        print('url open failed!')
    html = response.read().decode('utf-8')

    print('----测试方法----')
    file='day1-cookies.txt'
    save_cookies_to_file(file)
    read_cookies_from_file(file)
    print(cookies)
