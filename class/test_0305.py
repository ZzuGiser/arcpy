#coding:utf-8
'''
python 对象、函数和模块

'''
import sys
import xlrd
import xlwt
import random
import os
import time

def randong_fun():
    x = divmod(5, 2)  # 取模
    random.random()
    random.randint(1, 10)
    random.randrange(1, 10, 3)
    list1 = [1, 1, 2, 3, 4]
    random.choice(list1)
    random.sample(list1, 3)
    random.shuffle(list1)
'''
is前缀，able后缀。用于判断
交互式输入函数
'''
def file_readandWrite():
    file = open("e:/py/coor1.txt")
    for text in file:
        # type=chardet.detect(text)
        # text1=text.decode(type["encoding"])
        text1 = text.decode('gbk').encode('utf-8')
        print text1
    file.close()

    file = open("e:/py/coor1.txt")
    filew = open("e:/py/new2.txt", 'w')
    for text in file:
        text1 = text.decode('gbk').encode('utf-8')
        text2 = text1.replace("ID:", "")
        text3 = text2.replace("经度:", "")
        text4 = text3.replace("纬度:", "")
        text5 = text4.replace(",", " ")
        filew.writelines(text5 + "\n")
        filew.writelines("%s %s %s" % (text2, text3, text4))
        print text5
        '''
        text2=text1[4:5]
        text3=text1[15:22]
        text4=text1[32:38]
        '''
    file.close()
    filew.close()
    xlspath = r"e:\py\Lot.xls"
    data = xlrd.open_workbook(xlspath)
    table = data.sheets()[0]
'''
创建类和函数
'''
def printmessage(name,brithday):
        print ("hello")
        print("my name is %s"%name)
        print("I was born in %i"%brithday)
        age=time.localtime()[0]-brithday
        return age

myage=printmessage("Tom",1973)
print("Iam %i years old" % myage)



