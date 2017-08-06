#coding=utf-8
from database import Database
from table_opt import Table_opt
import filelib
import random

#随机生成一条选项
def generchose(data,indextrue ,mean ,id):
    slice = random.sample(data, 3)
    # print int('A')+1
    strl = ''
    cout = 1
    num =1
    realnum = indextrue;
    for i in range(1,5):
        if i== indextrue:
            cout = cout+1
            strl = strl + str(num) + ':' + mean +'\t'
            realnum = num;
            num=num+1
            continue
        if slice[i-cout][0]== id:
            continue
        strl =  strl + str(num) + ':' + slice[i-cout][4]+'\t'
        num=num+1

    return strl , realnum
    pass
#词义选择
#显示颜色格式：\033[显示方式;字体色;背景色m......[\033[0m]
"""
-------------------------------------------
-------------------------------------------
字体色     |       背景色     |      颜色描述
-------------------------------------------
30        |        40       |       黑色
31        |        41       |       红色
32        |        42       |       绿色
33        |        43       |       黃色
34        |        44       |       蓝色
35        |        45       |       紫红色
36        |        46       |       青蓝色
37        |        47       |       白色
-------------------------------------------
-------------------------------
显示方式     |      效果
-------------------------------
0           |     终端默认设置
1           |     高亮显示
4           |     使用下划线
5           |     闪烁
7           |     反白显示
8           |     不可见
-------------------------------
"""
def chosemean(maxnum):
    opt = Table_opt()
    data = opt.randfind(maxnum)
    ary = []
    for index in data:
        print index[1]
        #生成正确选项
        indextrue=random.randint(1,4)
        strl , realnum = generchose(data,indextrue, index[4] ,index[0])
        print strl
        chose = input("选择正确的选项:")
        if chose == realnum:
            print '\033[1;32m 正确 \033[0m'+'\n'
            ary.append(1)
        else:
            ary.append(0)
            print '\033[1;35m 错误 \033[0m'

            print '意思为:',

            print index[4]

            print ''
    showallword(data,ary)

def readinsertdata(path):
    opt = Table_opt()
    text =  filelib.readfile(path)
    dct = filelib.findcode(text)
    #opt = Table_opt()
    for key in dct:
        opt.insert(key,dct[key])
    print '文件读取录入完毕'

def showallword(data,ary):
    num = 0
    for index in data:
        if ary[num] == 0:
            print ('\033[1;35m%-50s%-50s\033[0m'%(index[1],index[4]))
        else:
            print ('%-50s%-50s'%(index[1],index[4]))
        num = num+1
