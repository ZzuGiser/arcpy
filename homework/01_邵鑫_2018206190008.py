import arcpy
from arcpy import env
env.workspace = "e:/py/data"
featureclasses = arcpy.ListFeatureClasses()
for fc in featureclasses:
    print fc
    cursor = arcpy.da.SearchCursor(fc, "*")
    for row in cursor:
        for i in range(len(row)):
            print row[i],
        print ""