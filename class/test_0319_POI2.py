#coding:utf-8
#百度地图POI搜索：单页面
import urllib,json,time
def create_json(url):
    url_file = urllib.urlopen(url)
    json_file = url_file.read()
    json_dict = json.loads(json_file)
    return json_dict
def read_json(json_dict,pois_list):
    for text in json_dict["results"]:
        poi_list = []
        poi_list.append(text["name"])
        poi_list.append(text["location"])
        poi_list.append(text["address"])
        pois_list.append(poi_list)
    return pois_list

def split_area(bound,bound_list):
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



ak = "bXs80o8GiDg6LE5rC7zMlVGKx5IgHVdm"
KeyWord = "武汉大学"
page_size = 20
page_num = 0
scope = 1
bound = [30.540273,114.360417,30.549694,114.369505]
pois_list = []   #创建存储所有POI信息的列表
#记数器
ai=0    #记录下载区域
bi=0    #记录下载页数
ci=0    #记录下载POI点数

bound_list=[bound]
count = 1
for bound in bound_list:
    url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + str(
        KeyWord) + "&bounds=" + str(bound[0]) + "," + str(bound[1]) + "," + str(bound[2]) + "," + str(
        bound[3]) + "&page_size=20"
    json_dict = create_json(url)
    pois_list = read_json(json_dict, pois_list)
    total = int(json_dict["total"])
    print("total"+str(total))

    if total < 400:
        ai +=1
        page_nums = total / 20
        if total % 20 > 0:
            page_nums += 1
        for page_num in range(0, page_nums):
            bi +=1
            time.sleep(4)
            url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + str(
                KeyWord) + "&bounds=" + str(bound[0]) + "," + str(bound[1]) + "," + str(bound[2]) + "," + str(
                bound[3]) + "&page_size=20" + "&page_num=" + str(page_num)
            json_dict = create_json(url)
            read_json(json_dict, pois_list)
    else:
        print("大于400")
        bound_list = split_area(bound,bound_list)


for poi_list in pois_list:
    ci += 1
    for text in poi_list:
        print text
print("共搜索区域%s, 搜索页数%s, 搜索到POI点数 %s"%(str(ai),str(bi),str(ci)))

