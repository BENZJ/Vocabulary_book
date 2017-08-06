#coding=utf-8
import re

# 读取文件中的内容 返回值为一个字符串形式的文件内容
def readfile(path):
    try:
        datafile = open(path)
        all_the_text = datafile.read( )
        datafile.close( )
        return all_the_text
    except Exception,e:
        print '路径有误'
        exit(1)

# 正则表达式读取所有画出的生词与含义 返回值为一个字典包含单词和含义
def findcode(text):
    pattern = re.compile(r'(?<=\().*?(?=\))')
    match = pattern.findall(text)
    pattern = re.compile(r'(?<=\[).*?(?=\])')
    match2 = pattern.findall(text)
    res = {}
    if len(match)!=len(match2):
        exit(1)
    else:
        for i in range(len(match)):
            res[match[i]] = match2[i]
    return res
