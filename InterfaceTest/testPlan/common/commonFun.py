import re
import json
import sys
import requests

sys.path
class Fun:
    #读取文件内容
    def take_token(path):
        with open(path, 'r') as load_f:
            load_dict = json.load(load_f)
            #for value in load_dict.values():
                #print("take_token获取成功:" + value)
                #return value
            print(load_dict)
            return load_dict
    #定义函数jsonFile用来保存获取的response到指定文件
    def save_to_jsonfile(file_name, contents):
        try:
            fh = open(file_name, 'w')
            fh.write(contents)
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("内容写入文件成功")
            fh.close()
    #定义函数getSession用来获取返回的sessionid和sessiondate
    def getSessionId(response):
        # 正则表达式截取返回结果的SessionID格式：res = r'<td>(.*?)</td><td>(.*?)</td>'
        res = r'<input type="hidden" name="sessionId" value="(.*?)"/>'
        m = re.findall(res, response, re.S | re.M)
        sessionid = str(m[0])
        return sessionid
    def getSessionId1(response):
        # 正则表达式截取返回结果的SessionID格式：res = r'<td>(.*?)</td><td>(.*?)</td>'
        try:
            res = r'<input type="hidden" name="sessionId" value="(.*?)"/>'
            m = re.findall(res, response, re.S | re.M)
            sessionid = str(m[0])
        except Exception as e:
            print(e)
        else:
            print("获取到SessionId")
            return sessionid
    #SessionData函数处理
    def getSessionData(response):
        # 正则表达式截取返回结果的SessionData格式：res = r'<td>(.*?)</td><td>(.*?)</td>'
        res = r'<input type="hidden" name="sessionData" value="(.*?)"/>'
        m = re.findall(res, response, re.S | re.M)
        sessiondata = str(m[0])
        return sessiondata
    def getSessionData1(response):
        # 正则表达式截取返回结果的SessionID格式：res = r'<td>(.*?)</td><td>(.*?)</td>'
        try:
            res = r'<input type="hidden" name="sessionData" value="(.*?)"/>'
            m = re.findall(res, response, re.S | re.M)
            sessiondata = str(m[0])
        except Exception as e:
            print(e)
        else:
            print("获取到SessionId")
            return sessiondata
    #两个字典类型合并的函数
    def merge_Two_Dicts(x,y):
        z = x.copy()
        z.update(y)
        return z
    #response数据重写
    def re_write(response1):
        user_info = '{\"bshtoken\" : \"' + response1 + '\"}'
        return user_info
    #定义get函数
    def get_url(url, params, headers):
        url = url
        params = params
        headers = headers
        response = requests.get(url=url, params=params, headers=headers)
        d = json.loads(response.text)
        print(response.text)
        assert response.status_code == 200
        assert d["retInfo"] == "success", "retInfo not right"
        assert "retBody" in d.keys()
        print("status_code_IPLocation:" + str(response.status_code))
        print("pass")

    # 定义post函数
    def post_url(url, data, headers):
        url = url
        data = data
        headers = headers
        response = requests.post(url, data, headers = headers)
        d = json.loads(response.text)
        print(response.text)
        assert response.status_code == 200
        assert d["retInfo"] == "success", "retInfo not right"
        assert "retBody" in d.keys()
        print("status_code_IPLocation:" + str(response.status_code))
        print("pass")

class Url:
    server1 = "https://api.home-connect.cn"
    server2 = "https://solution.home-connect.cn"

class Login_Element:
    server1 = "https://api.home-connect.cn"
    server2 = "https://solution.home-connect.cn"
    login_url1 = server1+"/security/oauth/authorize"
    login_url2 = server1+"/security/oauth/login"
    login_url3 = server2+"/sfmapi/getAuthToken"
    params1 = {'response_type': 'code',
               'client_id': '970F224CEB3BC18966E2A0564D00B88235FCB2753FCC9C98C1208199EF651F07'}
    header2 = {"Content-Type": "application/x-www-form-urlencoded",
               "client_id": "970F224CEB3BC18966E2A0564D00B88235FCB2753FCC9C98C1208199EF651F07"}
    header3 = {'Content-Type': 'application/x-www-form-urlencoded',
               'ha_id': 'SIEMENS-KA92NP49TI-68A40E005BA3',
               'device_code': '123456789'}
    message2 = {"client_id": "970F224CEB3BC18966E2A0564D00B88235FCB2753FCC9C98C1208199EF651F07",
                "email": "pcn90@grr.la",
                "password": "qwer1234!",
                }
class BasicSupport_Element:
    server2 = "https://solution.home-connect.cn"
    IPLocation_url = server2 + "/sfmapi/service/v1/ip/getCityInfo"
    header1 = {'Content-Type': 'application/json'}
    Realtimeweather_url = server2 + "/sfmapi/service/v1/weather/getWeather"
    header2 = {'Content-Type': 'application/json',
               'location':'nanjing',
               'language':'Zh-Hans',
               'unit':'c'}
    WeatherforecastInterface_url = server2 + "/sfmapi/service/v1/weather/future"
    header3 = {'Content-Type': 'application/json',
               'location': 'nanjing',
               'language': 'Zh-Hans',
               'unit': 'c',
               'start':'0',
               'days':'1'}
    TimeSynchronization_url = server2 + "/sfmapi/service/v1/weather/time"
    header4 = {
        'Content-Type': 'application/json'
    }

class Recipe_Interfaces:
    server2 = "https://solution.home-connect.cn"
    getRecipeCatalogs_url = server2 + "/sfmapi/service/v1/recipe/getRecipeCatalogs"
    header1 = {'Content-Type': 'application/json'}
    data1 = {"header":{"timestamp":"2014-11-12 15:48:00","deviceCode":"BE080A300QZ225H00002","ver":"v1.0","sign":"18c8c29f0898ac4b8b0a7a6afdb436aa"},"data":{}}
    getRecipeHotCatalogs_url =server2 + "/sfmapi/service/v1/recipe/getRecipeHotCatalogs"
    getRecipeList_url = server2 + "/sfmapi/service/v1/recipe/getRecipeList"
    data3={
	"header":{
		"timestamp":"2014-11-12 15:48:00",
		"deviceCode":"1111111",
		"ver":"v1.0",
		"sign":"18c8c29f0898ac4b8b0a7a6afdb436aa"},
	"data":{
		"kw":"牛肉",
		"order":"1",
		"ifmax":"1"},
	"offset":0,
	"pageSize":20}
    getSearchRecipe_url = server2 + "/sfmapi/service/v1/recipe/getSearchRecipe"
    data4={
	"header":{
		"timestamp":"2014-11-12 15:48:00",
		"deviceCode":"332131232",
		"ver":"v1.0",
		"sign":"18c8c29f0898ac4b8b0a7a6afdb436aa"},
	"data":{
		"kw":"鸡肉",
		"order":"1",
		"ifmax":"1"},
	"offset":0,
	"pageSize":20}
    GetRecipeDetails_url = server2 + "/sfmapi/service/v1/recipe/getRecipe"
    data5 = {
	"header":{"timestamp":"2014-11-12 15:48:00","deviceCode":"BE080A300QZ225H00002","ver":"v1.0","sign":"18c8c29f0898ac4b8b0a7a6afdb436aa"},
	"data":{"cook_id":"809327"}
    }