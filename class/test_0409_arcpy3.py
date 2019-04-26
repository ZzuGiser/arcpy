#coding:utf-8
'''
# @Title: homework
# @Description: 
# @author :邵鑫
# @date :2019/04
'''
import arcpy
from arcpy import env
from arcpy.sa import *
import copy
import numpy as np
in_data = "e:/py/data1/in_data/"
out_data = "e:/py/data1/out_data/"
myraster = "fhraster.img"
myrastertif="e:/py/data1/in_data/whtm1.tif/Band_1"

def cell_size(in_data, out_data, myraster):
    '''
    改变像素的分辨率
    :param in_data:输入路径
    :param out_data:输出路径
    :param myraster:原始数据
    :return:
    '''
    env.cellSize = 5
    arcpy.env.workspace = in_data
    out_raster =ApplyEnvironment(myraster)
    out_raster.save(out_data + "out_raster.img")

def desc_band(in_data, myraster):
    '''
    描述栅格数据
    :param in_data:
    :param myraster:
    :return:
    '''
    desc = arcpy.Describe(in_data + myraster)
    print(desc.height)  # 行数
    print(desc.width)          #列数
    print(desc.meanCellheight) #Y方向上像素大小
    print(desc.meanCellwidth)  #X方向上像素大小
    print(desc.primaryField)   #字段索引
    print(desc.tableType)      #表的类别名称

def mask_band(out_data, myraster):
    '''
    图像掩模运算
    :param out_data:
    :param myraster:
    :return:
    '''
    env.mask = "mask.shp"
    arcpy.env.workspace = in_data
    env.overwriteOutput = True
    mask_raster = ApplyEnvironment(myraster)
    mask_raster.save("img1.img")

def mask_image(in_data, out_data, myraster):
    '''
    图像掩模运算
    :param in_data:
    :param out_data:
    :param myraster:
    :return:
    '''
    outExtByMask = ExtractByMask(in_data + myraster, in_data + "mask.shp")
    outExtByMask.save(out_data + "img4.img")

def gray_stretch(raster,out_data):
    arcpy.env.workspace = out_data
    env.overwriteOutput = True
    myarray1 = arcpy.RasterToNumPyArray(raster, nodata_to_value=0)
    min_val = 255
    max_val = 0
    rows=len(myarray1)
    cols=len(myarray1[0])
    for i in range(0, rows - 1):
        for j in range(0, cols - 1):
            if myarray1[i][j] < min_val:
                min_val = myarray1[i][j ]
            elif myarray1[i][j] > max_val:
                max_val = myarray1[i][j]
    a=255/float(max_val-min_val)
    b=-255/float(max_val-min_val)*min_val
    for i in range(0, rows - 1):
        for j in range(0, cols - 1):
            myarray1[i][j]=int(myarray1[i][j]*a+b)
    outraster=arcpy.NumPyArrayToRaster(myarray1)
    outraster.save("graystretch1.tif")

def image_smooth(raster,out_path,smoothoperator):
    arcpy.env.workspace = out_data
    env.overwriteOutput = True
    myarray1 = arcpy.RasterToNumPyArray(raster, nodata_to_value=0)
    init=(len(smoothoperator)+1)/2-1
    rows=len(myarray1)
    cols=len(myarray1[0])
    for i in range(init, rows - 2):
        for j in range(init, cols - 2):
            myarrayoperator=myarray1[(i-init):(i+init+1),(j-init):(j+init+1)]
            element= myarrayoperator * smoothoperator
            myarray1[i,j]=np.sum(element)
    outraster=arcpy.NumPyArrayToRaster(myarray1)
    outraster.save("imagesmooth.tif")

def image_smooth2(raster,out_path,smoothoperator):
    arcpy.env.workspace = out_data
    env.overwriteOutput = True
    myarray1 = arcpy.RasterToNumPyArray(raster, nodata_to_value=0)
    myarray2=copy.copy(myarray1)
    init=(len(smoothoperator)+1)/2-1
    rows=len(myarray1)
    cols=len(myarray1[0])
    for i in range(init, rows - 2):
        for j in range(init, cols - 2):
            myarrayoperator=myarray1[(i-init):(i+init+1),(j-init):(j+init+1)]
            element= myarrayoperator * smoothoperator
            myarray2[i,j]=np.sum(element)
    outraster=arcpy.NumPyArrayToRaster(myarray2)
    outraster.save("imagesmooth2.tif")







if __name__ == "__main__":
    #cell_size(in_data, out_data, myraster)
    #myraster = "fhraster.img/Layer_1"
    #desc_band(in_data, myraster)
    # env.workspace=in_data
    # for raster in arcpy.ListRasters("fh*", "IMG"):
    #     print raster
    # myraster = "fhraster.img/Layer_1"
    # mask_band(out_data, myraster)
    # myraster = "fhraster.img"
    # mask_image(in_data, out_data, myraster)
    # gray_stretch(myrastertif,out_data)
    shape = (3, 3)
    operator =np.ones(shape)*1/9
    gray_stretch(myrastertif, out_data)
    image_smooth(myrastertif,out_data,operator)
    image_smooth2(myrastertif,out_data,operator)









