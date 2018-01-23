#! /usr/bin/env/python
#
# coding utf-8
#
# 爬取糗事百科
#
# jasonahven
#
'''
1.MMID
2.姓名
3.体重
4.城市
5.职业
6.风格
7.头像
8.写真
'''


class MM:
    def __init__(self, userId, realName, weight, city, occupation, style, avatarUrl, cardUrl):
        self.userId = userId
        self.realName = realName
        self.weight = weight
        self.city = city
        self.occupation = occupation
        self.style = style
        self.avatarUrl = avatarUrl
        self.cardUrl = cardUrl

    def __str__(self):
        return 'userId={} \n realName={}'.format(self.userId, self.realName)
