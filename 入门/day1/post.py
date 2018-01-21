#! /usr/bin/env/python
#
# coding utf-8
#
# jasonahven
#
#


import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }

    values={
        'username':'jasonahven',
        'password': '123456'
    }

    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, headers=headers, data=data)
    
    response = urllib.request.urlopen(request)

    print(response.status)
