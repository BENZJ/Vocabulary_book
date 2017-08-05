#coding=utf-8
# import filelib
#
# text =  filelib.readfile('../test.data')
# dct = filelib.findcode(text)
# print dct
#

import filelib
from database import Database
from table_opt import Table_opt
import functions as fuc
opt = Table_opt()
# text = filelib.readfile('../test.data')
# dct = filelib.findcode(text)
print '单词回顾系统'
print '1: 从文件中录入单词'
print '2: 单词回顾'
chose = raw_input('默认为[2]:')
if len(chose)==0:
    chose = '2'
if chose == '2':
    maxnum = raw_input('输入回顾单词数量[默认20]:')
    if len(maxnum) == 0:
        maxnum = '20'
    maxnum = int(maxnum)
    print '选择模式'
    print '1: 词义选择'
    print '2: 词汇选择'
    print '3: 词义拼写'
    print '4: 词汇拼写'
    childchose = raw_input('选择模式[默认1]:')
    if len(childchose) == 0:
        childchose = '1'
    childchose = int(childchose)
    if childchose == 1:
        fuc.chosemean(maxnum);


elif chose =='1':
    pass
else:
    print '错误输入'



# for key in dct:
#     opt.insert(key,dct[key])

# print opt.findword('xxxxx')
# print opt.findallnum()
# data = opt.randfind(2)
# print data[0][4]
# your_name = raw_input("".decode('utf-8').encode('utf-8'))
# print your_name
