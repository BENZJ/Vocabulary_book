#coding=utf-8
import mysql.connector
from mysql.connector import errorcode
from setting import Setting
"""
数据库结结构
----------------------------------------------
id     | word  | mean | intimes   | outtimes
----------------------------------------------
id主键  | 生词  | 解释  | 生词输入次数| 生词回顾次数
----------------------------------------------

链接数据库
方法1 链接数据库

方法2 检查数据库中单词是否已经存在并且返回id值若不存在返回-1

方法3 将指定id的单词intimes+1

方法4 插入单词，初始化生词输入次数为1，生词回顾次数为

"""
class Database(object):
    def __init__(self):
        self.cnx = None
        self.cursor = None

    def closecnx(self):
        self.cursor.close()
        self.cnx.close()

    def opencnx(self):
        self.cnx = mysql.connector.connect(
        user= Setting.databaseuser,
        password= Setting.databasepwd,
        host= Setting.host,
        database= Setting.databasename,
        buffered= True,
        )
        self.cursor = self.cnx.cursor()
