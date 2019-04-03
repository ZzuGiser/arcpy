
#coding:utf-8
# try:
#     print("aaa"+2)
# except:
#     print("Error!\n")
'''
Clip_analysis 剪切
'''
# import arcpy
# from arcpy import env
# try:
#     env.workspace = 'e:/py/data'
#     in_cover=arcpy.GetParameterAsText(0)
#     clip_cover=arcpy.GetParameterAsText(1)
#     out_cover=arcpy.GetParameterAsText(2)
#     arcpy.Clip_analysis(in_cover, clip_cover, out_cover)
# except:
#     print "error!\n"

'''
Split_analysis 分割
'''
# import arcpy
# arcpy.env.workspace = "e:/py/data"
# arcpy.Split_analysis("hydpy.shp", "split.shp", "spli", "G:/f_data/Default.gdb", "1 Meters")

'''
Describe 文件描述
'''
# import arcpy
# file ="e:/py/data/clip.shp"
# file_desc=arcpy.Describe(file)
# print (file_desc.shapeFieldName)
# print(file_desc.Name)
# print (file_desc.Shapetype)
#
# for child in file_desc.children:
#     print "\t%s = %s" % (child.name, child.dataType)

'''
ListFeatureClasses 文件列表
'''
# import arcpy
# from arcpy import env
# env.workspace = "e:/py/data"
# featureclasses = arcpy.ListFeatureClasses()
# # Copy shapefiles to a file geodatabase
# for fc in featureclasses:
#     env.workspace = "e:/py/data/"+fc
#     fields = arcpy.ListFields()
#     for field in featureclasses:
#         print field
'''
SearchCursor shp的属性查看
'''
# import arcpy
# from arcpy import env
# env.workspace = "e:/py/data"
# file = "split.shp"
# cursor=arcpy.da.SearchCursor(file,"spli")
# for row in cursor:
#     print (row[0])

'''
SearchCursor shp的属性查看2
'''
# import arcpy
# from arcpy import env
# env.workspace = "e:/py/data"
# file = "fhpoi.shp"
# cursor=arcpy.da.SearchCursor(file,"*")
# for row in cursor:
#     for i in range(len(row)):
#         print(row[i])
'''
目录下所有图层所有字段
'''
# import arcpy
# from arcpy import env
# env.workspace = "e:/py/data"
# featureclasses = arcpy.ListFeatureClasses()
# for fc in featureclasses:
#     cursor = arcpy.da.SearchCursor(fc, "*")
#     for row in cursor:
#         for i in range(len(row)):
#             print(row[i])

'''
指定路径下所有图层所有字段
'''
# import arcpy
# from arcpy import env
# filew = open("e:/py/data/new2.txt", 'w')
# env.workspace = "e:/py/data"
# featureclasses = arcpy.ListFeatureClasses()
# for fc in featureclasses:
#     cursor = arcpy.da.SearchCursor(fc, "*")
#     for row in cursor:
#         for i in range(len(row)):
#             filew.writelines(i)
#         filew.writelines("\n")
# file.close()


# import arcpy
# from arcpy import env
# env.workspace = "c:/py/data"
# featureclasses = arcpy.ListFeatureClasses()
# for fc in featureclasses:
#     print fc
#     cursor = arcpy.da.SearchCursor(fc, "*")
#     for row in cursor:
#         for i in range(len(row)):
#             print row[i],
#         print ""