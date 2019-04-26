#coding:utf-8
'''
# @Title: homework
# @Description: 
# @author :邵鑫
# @date :2019/04
'''
import arcpy
mymxd = "e:/py/data/in_data/test.mxd"
mymxd1 = "e:/py/data/in_data/test1.mxd"
mymxd2= "e:/py/data/in_data/homework.mxd"

def MapDocument(mymxd):
    '''
    配置属性
    :param mymxd:
    :return:
    '''
    mymap = arcpy.mapping.MapDocument(mymxd)
    print(mymap.title)
    print(mymap.summary)
    print(mymap.description)
    print(mymap.author)
    print(mymap.credits)
    print(mymap.tags)
    print(mymap.hyperlinkBase)
def ListLayer(mymxd):
    '''
    图层名
    :param mymxd:
    :return:
    '''
    mymap = arcpy.mapping.MapDocument(mymxd)
    mydfs = arcpy.mapping.ListDataFrames(mymap)
    for mydf in mydfs:
        layers = arcpy.mapping.ListLayers(mymap, "", mydf)
        layers = arcpy.mapping.ListLayers(mymap)
        for layer in layers:
            print(layer.name)
def LayerLaber(mymxd):
    '''
    图层标注
    :param mymxd:
    :return:
    '''
    mymap = arcpy.mapping.MapDocument(mymxd)
    layers = arcpy.mapping.ListLayers(mymap)
    layer = layers[0]
    layer.showLabels = True
    layer.labelClasses[0].expression = '[x坐标] + ","+[y坐标]'
    mymap.save()
def AddLayer(mymxd):
    mymap = arcpy.mapping.MapDocument(mymxd)
    df = arcpy.mapping.ListDataFrames(mymap)[0]
    mylayer = arcpy.mapping.Layer("e:/py/data/clip.lyr")
    arcpy.mapping.AddLayer(df, mylayer)
    mymap.save()
def DataRenderingOutput(mymxd):
    mymap = arcpy.mapping.MapDocument(mymxd)
    layers = arcpy.mapping.ListLayers(mymap)
    for layer in layers:
        layer.showLabels = True
        layer.labelClasses[0].expression = '[NAME]'
    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()
    mypdf = arcpy.mapping.PDFDocumentCreate("e:/data/newpdf.pdf")
    lyr = arcpy.mapping.ListLayers(mymap)[4]
    df = arcpy.mapping.ListDataFrames(mymap)[0]
    rows = arcpy.SearchCursor(lyr)
    for row in rows:
        geo = row.shape
        # df.zoomToSelectedFeatures()
        df.panToExtent(geo.extent)
        outFile = "e://data//" + row.getValue("NAME") + ".pdf"
        outFile1=outFile.replace('?', '')
        arcpy.mapping.ExportToPDF(mymap, outFile1)
        mypdf.appendPages(outFile1)
    mypdf.saveAndClose()
    mymap.save()


    # lyr = arcpy.mapping.ListLayers(mymap)[4]
    # df = arcpy.mapping.ListDataFrames(mymap)[0]
    # rows = arcpy.SearchCursor(lyr)
    # for row in rows:
    #     geo = row.shape
    #     df.panToExtent(geo.extent)
    #     outFile = r"d:\data\\" + row.getValue("NAME") + ".pdf"
    #     arcpy.mapping.ExportToPDF(mymap, outFile)
    # mymap.saveAndClose()

    #layers = arcpy.mapping.ListLayers(mymap)
    # for layer in layers:
    #     layer.showLabels = True
    #     layer.labelClasses[0].expression = '[NAME]'
    # arcpy.RefreshTOC()
    # arcpy.RefreshActiveView()

if __name__=="__main__":
    # MapDocument(mymxd)
    # ListLayer(mymxd)
    #LayerLaber(mymxd1)
    DataRenderingOutput(mymxd2)
