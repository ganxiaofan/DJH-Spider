#! /usr/bin/env/python
#
# coding utf-8
#
# 爬取淘宝MM
#
# jasonahven
#
'''
将信息保存在数据库中
将头像和写真按照文件夹保存
'''
import os
from mm import MM
import urllib.request
import pymysql


def mkdirs(root, mms):
    # 去除首位空格
    path = root.strip()

    # 判断路径是否存在
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)

    # 创建个人目录
    try:
        for mm in mms:
            userId = mm.userId
            realName = mm.realName
            dir = '{0}-{1}'.format(userId, realName)
            path = root + "\\" + dir
            os.makedirs(path)
            print('创建MM目录: {0}-{1} 成功'.format(userId, realName))
        return True
    except Exception as e:
        print(e)
        return False


def save_photos(mms):
    '''
    下载图片并保存
    '''
    root = "实战\\淘宝MM照片\\mmphotos"
    mkdirs(root, mms)

    for mm in mms:
        try:
            # 头像
            avatarUrl = mm.avatarUrl
            avatar_suffix = avatarUrl[-4:]
            avatar_path = 'https:' + avatarUrl
            resp = urllib.request.urlopen(avatar_path)

            userId = mm.userId
            realName = mm.realName
            dir = '{0}-{1}'.format(userId, realName)
            file = root + '\\' + dir + '\\' + 'avatar' + avatar_suffix

            f = open(file, "wb")
            f.write(resp.read())
            f.flush()
            f.close()
            print('保存MM头像: {0}-{1} 成功'.format(userId, realName))

            # 写真
            cardUrl = mm.cardUrl
            card_suffix = cardUrl[-4:]
            card_path = 'https:' + cardUrl
            resp = urllib.request.urlopen(card_path)
            file = root + '\\' + dir + '\\' + 'card' + card_suffix
            f = open(file, "wb")
            f.write(resp.read())
            f.flush()
            f.close()
            print('保存MM写真: {0}-{1} 成功'.format(userId, realName))
        except Exception as e:
            print('保存MM图片: {0}-{1} 有问题'.format(userId, realName), e)
            continue


def save_info(user, pwd, db, table, mms):
    '''
    将信息保存在数据库中
    '''
    # 数据库连接:pymysql 正常情况下会尝试将所有的内容转为latin1字符集处理
    db = pymysql.connect("localhost", "root", "root",
                         "taobao", use_unicode=True, charset="utf8")
    if db != None:
        print('数据库链接成功')
    else:
        print('数据库链接失败')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    '''
    # 如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS mm")

    # 使用预处理语句创建表
    sql = """CREATE TABLE mm (
            userId  varchar(20) not null,
            realName  varchar(20) not null,
            weight varchar(20) ,
            city varchar(20) ,
            occupation varchar(20) ,
            style varchar(20) ,
            avatarUrl varchar(100) ,
            cardUrl varchar(100) 
            )"""
    cursor.execute(sql)
    '''
    for mm in mms:
        userId = mm.userId
        realName = mm.realName
        weight = mm.weight
        city = mm.city
        occupation = mm.occupation
        style = mm.style
        avatarUrl = mm.avatarUrl
        cardUrl = mm.cardUrl
        
        try:
            # SQL 插入语句
            #sql = "INSERT INTO {0} VALUES({1},{2},{3},{4},{5},{6},{7},{8})".format(table, "12", "12", "12", "12", "12", "12", "12", "12")
            
            sql = 'INSERT INTO {0} VALUES("{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(table,  userId,  realName,  weight,  city,  occupation,  style,  avatarUrl,  cardUrl)

            # 执行sql语句
            print('执行SQL语句保存MM信息: {0}-{1} '.format(userId, realName))
            cursor.execute(sql)

            # 提交到数据库执行
            db.commit()
            print('保存MM信息: {0}-{1} 成功'.format(userId, realName))
        except Exception as e:
            # 如果发生错误则回滚
            print('保存MM信息: {0}-{1} 回滚'.format(userId, realName), e)
            db.rollback()

    # 关闭数据库连接
    db.close()
    print('关闭数据库')


if __name__ == "__main__":
    root = "实战\\淘宝MM照片\\mmphotos"

    mm1 = MM('1', '2', '1', '2', '1', '2', '1', '2')
    mm2 = MM('11', '2', '1', '2', '1', '2', '1', '2')
    mms = [mm1, mm2]

    user = 'root'
    pwd = 'root'
    db = 'taobao'
    table = 'mm'
    save_info(user, pwd, db, table, mms)
