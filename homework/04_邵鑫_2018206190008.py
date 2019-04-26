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
myrastertif="e:/py/data1/in_data/whtm1.tif/Band_1"


def gray_stretch(raster,out_path):
    '''
    图像线性拉伸
    :param raster:原始数据
    :param out_path: 输出结果路径
    :return:
    '''
    arcpy.env.workspace = out_path
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
    '''
    图像平滑(串行计算)
    :param raster:原始数据
    :param out_path: 输出结果路径
    :param smoothoperator: 平滑算子
    :return:
    '''
    arcpy.env.workspace = out_path
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
    '''
    图像平滑(并行计算)
    :param raster:原始数据
    :param out_path: 输出结果路径
    :param smoothoperator: 平滑算子
    :return:
    '''
    arcpy.env.workspace = out_path
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
    shape = (3, 3)
    operator =np.ones(shape)*1/9
    gray_stretch(myrastertif, out_data)
    image_smooth(myrastertif,out_data,operator)
    image_smooth2(myrastertif,out_data,operator)
