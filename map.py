import json
from urllib.request import urlopen, quote
import requests


while True:
    def getlnglat(address):
        url = 'http://api.map.baidu.com/geocoding/v3/'
        address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
        output = 'json'
        ak = '密钥' 
        # 浏览器端密钥，需要登陆百度地图申请
        callback = 'showLocation'
        uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak + '&callback=' + callback
        req = urlopen(uri)
        res = req.read().decode()
        res=res[27:-1]
        temp = json.loads(res)
        lng = temp['result']['location']['lng'] #经度
        lat = temp['result']['location']['lat'] #纬度
        return lng, lat

    inpt = input("请输入地址：")
    adr=getlnglat(inpt)
    print("地点经度：",adr[0],"地点维度：",adr[1])
