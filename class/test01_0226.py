#coding:utf-8
'''
list 列表
'''
x=[9,3,4]
x.sort()
print x
[3, 4, 9]
#元组与列表的唯一不同是不能修改
'''
元组 tuple
'''
x=1,2,3
print x
(1, 2, 3)
x=(1)#相当于数学运算的括号
print x
#1
x=(1,)#定义元组
print x
#(1,)
x=3*(10+2,)
print x
#(12, 12, 12)
y=tuple(x)
print y
#(1, 2) 列表与元组的转化
'''
字典 Key:Vlaue
字典不能相乘和连接，没有顺序
'''
dict={}
dict["shao"]="xin"
print dict["shao"]
#   xin
dict={"shao":"xin","zhang":"han"}
print dict
#   {'shao': 'xin', 'zhang': 'han'}
dict.keys()
#   ['shao', 'zhang']
del dict["shao"]
print dict
#   {'zhang': 'han'}
'''
流程控制
'''
import random
x = random.randint(1,100)
if x < 60:
    print "level=D"
elif x >= 60 and x<= 90:
    print "level=B"
else:
    print "Level=A"
#判断坐标在第几象限
x=int(input('please input x aixse size:x='))
y=int(input('please input x aixse size:x='))
if x>=0:
    if y >= 0:
        print('坐标（%i,%i）,在第一象限'%(x,y))
    else:
        print('坐标（%i,%i）,在第四象限'%(x,y))

else:
    if y >= 0:
        print('坐标（%i,%i）,在第二象限'%(x,y))
    else:
        print('坐标（%i,%i）,在第三象限'%(x,y))
#猜数字
import random
guess=random.randint(1,100)
ii=0
Nums=input("输入次数")
while ii<int(Nums):
    ii+=1
    kk=input("请输入猜想数字：")
    if int(kk)==guess:
        print("猜对了")
        break
    elif int(kk)>guess:
        print ('猜大了')
    else:
        print ('猜小了')
'''
格式化输出
'''
z=1.24234
print("%.3f"%(z))
#1.242
print("%5.1f"%(z))
#  1.2
print("%-5.1f"%(z))
#1.2
#for 循环语句
