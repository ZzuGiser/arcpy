#coding:utf-8
'''
# @Title: homework
# @Description: 属性创建和多个面的绘制
# @author :邵鑫
# @date :2019/04
'''
import arcpy
import fileinput
def copyfield(in_path,tem_shp,out_path,new_poly):
    '''
    新建面要素并将tem_shp的属性复制过来
    :param in_path: 模板图层路径
    :param tem_shp: 模板图层名
    :param out_path: 新建图层路径
    :param new_poly: 新建图层名
    :return:
    '''
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


def AddPolygonFeature(in_path,tem_shp,in_file,out_path,new_poly):
    '''
    以tem_shp为模板新建一个面图层，并读取in_file完成多个面的绘制
    :param in_path: 模板图层路径
    :param tem_shp:模板图层名
    :param in_file:绘制面的坐标数据信息
    :param out_path:输出图层路径
    :param new_poly:输出图层名
    :return:
    '''
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

in_path="E:/py/data/in_data/"
out_path="E:/py/data/out_data/"
tem_shp="clip.shp";in_file="clip1.txt";new_poly="new_poly.shp"
copyfield(in_path,tem_shp,out_path,new_poly)                    #图层属性的拷贝
AddPolygonFeature(in_path,tem_shp,in_file,out_path,new_poly)    #多个面的绘制
