#coding:utf-8
'''
# @Title: homework
# @Description: 寻找武汉市中学范围500米所有的网吧
# @author :邵鑫
# @date :2019/03
'''
import urllib,json,time
def create_json(url):
    '''
    百度地图POI：根据URL下载POI数据并转换成JSON格式
    :param url: 需要下载的URL地址
    :return: 以JSON格式返回下载内容
    '''
    url_file = urllib.urlopen(url)
    json_file = url_file.read()
    json_dict = json.loads(json_file)
    return json_dict
def readweb_json(json_dict,pois_list):
    '''
    百度地图POI：对JSON数据进行解析
    :param json_dict: JSON格式的下载内容
    :param pois_list: 存储所有POI点信息
    :return:
    '''
    for text in json_dict["results"]:
        poi_list = []
        poi_list.append(text["name"])
        pois_list.append(poi_list)
    return pois_list
def readschool_json(json_dict,pois_list):
    '''
    百度地图POI：对JSON数据进行解析
    :param json_dict: JSON格式的下载内容
    :param pois_list: 存储所有POI点信息
    :return:
    '''
    for text in json_dict["results"]:
        poi_list = []
        poi_list.append(text["name"])
        #print(text["name"])
        poi_list.append(text["location"]["lat"])
        poi_list.append(text["location"]["lng"])
        pois_list.append(poi_list)
    return pois_list
def split_area(bound,bound_list):
    '''
    百度地图POI：对大数据范围进行分块
    :param bound:当前处理区域
    :param bound_list:下载区域列表
    :return:
    '''
    row_num = 2
    step_lat = (bound[2]- bound[0])/row_num
    step_lon = (bound[3] - bound[1]) / row_num
    for i in range (0,row_num):
        for j in range(0,row_num):
            bound_temp = []
            bound_temp.append(bound[0]+step_lat*i)
            bound_temp.append(bound[1] + step_lon * j)
            bound_temp.append(bound[0] + step_lat * (i+1))
            bound_temp.append(bound[1] + step_lon * (j+1))
            bound_list.append(bound_temp)
    return bound_list
def internetcafe_filter(school_list,school_counter):
    '''
    根据学校位置找到周边500米的网吧
    :param school_list: 当前处理学校的经纬度位置
    :param school_counter: 当前处理学校的序号
    :return:
    '''
    web_counter=0
    webs_list = []
    url = "http://api.map.baidu.com/place/v2/search?query=网吧&location=" + str(school_list[0]) + "," + \
          str(school_list[
                  1]) + "&radius=500&output=json&ak=cZ1YEgywP0brUYtYf5flTWe005ZrIwhQ&page_size=20&page_num=0"
    json_dict = create_json(url)
    total = int(json_dict["total"])
    page_nums = total / 20
    if total % 20 > 0:
        page_nums += 1
    for page_num in range(0, page_nums):
        time.sleep(4)
        url = "http://api.map.baidu.com/place/v2/search?query=网吧&location=" + str(
            school_list[0]) + "," + str(school_list[
                                            1]) + "&radius=500&output=json&ak=cZ1YEgywP0brUYtYf5flTWe005ZrIwhQ&page_size=20" + "&page_num=" + str(page_num)
        json_dict = create_json(url)
        readweb_json(json_dict, webs_list)
        for web_poi in webs_list:
            web_counter +=1
            print("%s_%s. %s" % (str(school_counter),str(web_counter), web_poi[0]))
            filew.writelines("%s_%s. %s\n" % (str(school_counter),str(web_counter), web_poi[0].encode('utf-8')))
def load_school(bound_list,ak ,KeyWord):
    '''
    下载指定区域的的学校的POI信息
    :param bound_list: 指定下载范围
    :param url_area: URL地址
    :return:
    '''
    school_counter=0
    schoolpois_list = []  # 创建存储所有学校POI信息的列表
    for bound in bound_list:
        url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + str(
            KeyWord) + "&bounds=" + str(bound[0]) + "," + str(bound[1]) + "," + str(bound[2]) + "," + str(
                bound[3]) + "&page_size=20"
        json_dict = create_json(url)
        total = int(json_dict["total"])
        print("total：" + str(total))
        if total < 400:
            page_nums = total / 20
            if total % 20 > 0:
                page_nums += 1
            for page_num in range(0, page_nums):
                time.sleep(4)
                url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + str(
                    KeyWord) + "&bounds=" + str(bound[0]) + "," + str(bound[1]) + "," + str(bound[2]) + "," + str(
                    bound[3]) + "&page_size=20" + "&page_num=" + str(page_num)
                json_dict = create_json(url)
                readschool_json(json_dict, schoolpois_list)
        else:
            print("大于400")
            bound_list = split_area(bound, bound_list)

    for schoolpoi_list in schoolpois_list:
        school_counter +=1
        school_location = []
        print ("%s.%s" % (str(school_counter), schoolpoi_list[0]))
        filew.write("%s. %s\n" % (str(school_counter),schoolpoi_list[0].encode('utf-8')))
        school_location.append(schoolpoi_list[1])
        school_location.append(schoolpoi_list[2])
        internetcafe_filter(school_location,school_counter)


filew = open("e:/py/schoolweb.txt", 'w')
ak = "PqF61jD52cUG4eLI8TYETsDqW7QizeHE"
KeyWord = "中学"
page_size = 20
page_num = 0
scope = 1
bound = [30.482263,114.072493,30.78343,114.559303]
bound_list=[bound]
load_school(bound_list,ak ,KeyWord)
filew.close()





