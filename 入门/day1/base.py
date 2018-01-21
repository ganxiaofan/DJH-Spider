#! /usr/bin/env/python
#
# coding utf-8
#
# jasonahven
#
# urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# urllib.request.urlopen(url, data=None, timeout=<object object at 0x000001B71FA69420>, *, cafile=None, capath=None, cadefault=False, context=None)


import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }

    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request)
    print(response.status)
