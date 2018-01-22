#! /usr/bin/env/python
#
# coding utf-8
#
# 爬取糗事百科
#
# jasonahven
#


class Joke:
    def __init__(self, author, content, like, comment):
        self.author = author
        self.content = content
        self.like = like
        self.comment = comment

    def __str__(self):
        return 'author={}\ncontent={}\nlike={}\ncomment={}'.format(self.author, self.content, self.like, self.comment)
