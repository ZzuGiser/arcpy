#coding:utf-8
import urllib,json
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
#url=r'http://api.map.baidu.com/place/v2/search?query=武汉大学&bounds=30.349715,113.864292,30.922445,115.050918&output=json&ak=cZ1YEgywP0brUYtYf5flTWe005ZrIwhQ&page_size=20&page_num=0'

ak = "bXs80o8GiDg6LE5rC7zMlVGKx5IgHVdm"
KeyWord = "武汉大学"
page_size = 20
page_num = 0
scope = 1
bound = [30.542273,114.363417,30.545694,114.367505]
pois_list = []   #创建存储所有POI信息的列表
url = "http://api.map.baidu.com/place/v2/search?ak="+str(ak)+"&output=json&query="+str(KeyWord)+"&bounds="+str(bound[0])+","+str(bound[1])+","+str(bound[2])+","+str(bound[3])+"&page_size=20"
json_dict = create_json(url)
pois_list = read_json(json_dict,pois_list)
total = int(json_dict["total"])

for poi_list in pois_list:
    for text in poi_list:
        print text


