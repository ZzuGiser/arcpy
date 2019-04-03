#coding:utf-8
'''
# @Title: homework
# @Description: 
# @author :邵鑫
# @date :2019/04
'''
import arcpy
import fileinput
def deleteRow(file):
    '''
    删除指定的字段
    :param file: 需要删除的文件
    :return:
    '''
    cursor = arcpy.da.UpdateCursor(file, ["GB"])  # 字段括起来，否则不认为是参数
    for row in cursor:
        if (row[0] == 42024):
         cursor.deleteRow()
    del cursor,row

def Insert_Cursor(file):
    '''
    在属性表中插入一个要素
    :param file:
    :return:
    '''
    cursor = arcpy.da.InsertCursor(file, ["town","road","building"])  # 字段括起来，否则不认为是参数
    cursor.insertRow(("aa","bb","cc"))
    del cursor

def addfeature(file):
    '''
    在指定图层中添加一个要素
    :param file:
    :return:
    '''
    cursor=arcpy.da.InsertCursor(file,["OBJECTID","SHAPE@XY"])
    cursor.insertRow((50000,(50000,50000)))

def newfile():
    '''
    新建一个点图层
    :return:
    '''
    path="E:/py/data"
    file="new_file"
    geometry_type="POINT"
    template="fhpoi.shp"
    if arcpy.Exists(file)==False:
        arcpy.CreateFeatureclass_management(path,file,geometry_type,template)


def AddPolygonFeature():
    '''
    创建面图层并添加要素
    :return:
    '''
    in_path="E:/py/data/in_data/"
    out_path="E:/py/data/out_data/"
    tem_shp="clip.shp";in_file="clip.txt";new_poly="new_poly.shp"
    if arcpy.Exists(out_path + new_poly):
        arcpy.Delete_management(out_path + new_poly)
    arcpy.CreateFeatureclass_management(out_path,new_poly,"POLYGON",in_path + tem_shp)
    cursor=arcpy.da.InsertCursor(out_path+new_poly,"shape@")
    array=arcpy.Array()
    point=arcpy.Point()
    polylist=[]
    i=1
    for line in fileinput.input(in_path+in_file):
        if line.replace("\n","")==str(i):
            i +=1
            if i>2:
                polylist.append(array)
                array=arcpy.Array()
        else:
            point.ID, point.X, point.Y = line.split()
            array.add(point)
    polylist.append(array)
    for var in polylist:
        polygon = arcpy.Polygon(var)
        cursor.insertRow([polygon])

    fileinput.close()
    del cursor, line
def copyfield(in_path,tem_shp,out_path,new_poly):
    '''
    新建面要素并将tem_shp的属性复制过来
    :param in_path: 模板图层路径
    :param tem_shp: 模板图层名
    :param out_path: 新建图层路径
    :param new_poly: 新建图层名
    :return:
    '''
    in_path="E:/py/data/in_data/"
    out_path="E:/py/data/out_data/"
    tem_shp="clip.shp";in_file="clip.txt";new_poly="new_poly.shp"
    file = in_path + tem_shp
    fields = arcpy.ListFields(file)
    fieldlist = []
    for field in fields:
        fielditr = [field.name, field.type]
        fieldlist.append(fielditr)
    if arcpy.Exists(out_path + new_poly):
        arcpy.Delete_management(out_path + new_poly)
    arcpy.CreateFeatureclass_management(out_path, new_poly, "POLYGON")
    arcpy.env.workspace = out_path
    for var in fieldlist:
        if var[0] == "FID" or var[0] == "Shape" or var[0] == "Id":
            continue
        else:
            arcpy.AddField_management(new_poly, var[0], var[1])








