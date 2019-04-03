#coding:utf-8
'''
# @Title: homework
# @Description: 
# @author :邵鑫
# @date :2019/03
'''

import arcpy
def Pointfeaturetraversal():
    '''
    遍历shp文件的各个要素的重心
    :return:
    '''
    arcpy.env.workspace = "E:/py/data"
    file = "fhpoi.shp"
    cursor = arcpy.da.SearchCursor(file, "SHAPE@XY")
    for row in cursor:
        print row[0]

def PolylinePointfeaturetraversal():
    '''
    遍历折线shp文件的各个要素的折点
    :return:
    '''
    arcpy.env.workspace = "E:/py/data"
    file = "road.shp"
    cursor = arcpy.da.SearchCursor(file, ["SHAPE@"])
    i=0
    #每条线的信息
    for row in cursor:
        i +=1
        print(i)
        #每条线中的每个点
        for pnts in row[0]:
            #每个点详细信息
            for pnt in pnts:
                print pnt
def PolylineLength():
    '''
    计算图层中线段的总长度
    :return:
    '''
    arcpy.env.workspace = "E:/py/data"
    file = "road.shp"
    cursor = arcpy.da.SearchCursor(file, "SHAPE@LENGTH")
    cursorsum=0
    #每条线的信息
    for row in cursor:
        print(row)
        cursorsum +=row[0]
    print(cursorsum)


def Polylinefilter(str):
    '''
    对Polyline按照属性进行筛选
    :return:
    '''
    arcpy.env.workspace = "E:/py/data"
    file = "pipeline.shp"
    filter="material="+str
    cursor = arcpy.da.SearchCursor(file, "SHAPE_Leng",filter)
    cursorsum=0
    for row in cursor:
        cursorsum +=row[0]
    print cursorsum
'''
meterials=["'砼'","'塑'","'钢'","'铜'"]
for meterral in meterials:
    Polylinefilter(meterral)
'''

def Polylinefilter2():
    '''
    对Polyline按照属性进行筛选—方法二
    :return:
    '''
    arcpy.env.workspace = "E:/py/data"
    file = "pipeline.shp"
    cursor = arcpy.da.SearchCursor(file, ["material","SHAPE_Leng"])
    lengthsum=[0.0,0.0,0.0,0.0]
    length={'铜':'0','钢':'0','砼':'0','塑':'0'}
    for row in  cursor:
        key =row[0];value=row[1]
        if key in length.keys():
            value+=float(length[key])
            length[key]=str(value)
        else:
            length[key]=str(value)
    for key in length:
        print(key +":"+str(length[key]))
    for row in cursor:
        if row[1].encode("utf-8")=="铜":
            lengthsum[0] +=row[0]
        elif row[1].encode("utf-8")=="钢":
            lengthsum[1] +=row[0]
        elif row[1].encode("utf-8") == "砼":
            lengthsum[2] += row[0]
        elif row[1].encode("utf-8") == "塑":
            lengthsum[3] += row[0]
        else:
            continue
    #print lengthsum

def Modifyfield():
    '''
    修改字符值
    :return:
    '''
    arcpy.env.workspace = "E:/py/data"
    file = "fhpoi.shp"
    cursor = arcpy.da.UpdateCursor(file, "town")
    for field in cursor:
        field[0]='abc'
        cursor.updateRow(field)

def Scraptime():
    '''
    修改字符值(字段组合)
    :return:
    '''
    arcpy.env.workspace = "E:/py/data"
    file = "pipeline.shp"
    cursor = arcpy.da.UpdateCursor(file, ["LayDate","DisusDate","material"])
    for row in cursor:
        print row
        print row[0].encode("utf-8")
        if row[2].encode("utf-8")=="铜":
            if row[0].encode("utf-8")==" ":
                row[1] = str(2019 + 30)
            else:
                row[1] = int(row[0].encode("utf-8"))+30
        elif row[2].encode("utf-8")=="钢":
            if row[0].encode("utf-8")==" ":
                row[1] = str(2019 + 30)
            else:
                row[1] = int(row[0].encode("utf-8"))+30
        elif row[2].encode("utf-8") == "砼":
            if row[0].encode("utf-8")==" ":
                row[1] = str(2019 + 30)
            else:
                row[1] = int(row[0].encode("utf-8"))+30
        elif row[2].encode("utf-8") == "塑":
            if row[0].encode("utf-8")==" ":
                row[1] = str(2019 + 30)
            else:
                row[1] = int(row[0].encode("utf-8"))+30
        else:
            continue
        cursor.updateRow(row)


Polylinefilter2()


