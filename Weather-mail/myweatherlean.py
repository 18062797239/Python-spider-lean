#!/usr/bin/env python
# -*- coding:utf-8 -*-  
"""
@author: YuFei 
@email: yufei6808@163.com
@site: http://www.antuan.com
@version: 0.0.1
@date: 2018-08-23
@explain: 功能介绍
"""

from json import *
import urllib.request
import re
from python import weather24
from playhouse.sqlite_udf import tonumber

def getrequest(url):
    html=urllib.request.urlopen(link) #就可以访问了，不会报异常
    rehtml = html.read().decode('utf-8')#读入打开的url
    rejson = JSONDecoder().decode(rehtml)#创建json
    if rejson['status'] == 200:
        return rejson
    return 0

def getwinfo(winfo):
    '''
    forecast{
    "date": "31日星期三",
    "sunrise": "06:25",
    "high": "高温 23.0℃",
    "low": "低温 9.0℃",
    "sunset": "17:23",
    "aqi": 68.0,
    "fx": "东风",
    "fl": "<3级",
    "type": "晴",
    "notice": "愿你拥有比阳光明媚的心情"
    }
    '''
    print(winfo)
    
    for key in winfo:
        print(key,winfo[key])
        if key == "date":
            date = winfo['date']
            pattern = re.compile('(\d+)(.*)')
            result = pattern.findall(date)
            date = result[0][0]
            week = result[0][1]
        if key == "high":
            high = winfo['high']
            pattern = re.compile('.*(\d+\d+.\d+).*')
            result = pattern.findall(high)
            high = result[0]
        if key == "low":
            low = winfo['low']
            pattern = re.compile('.*(\d+\d+.\d+).*')
            result = pattern.findall(low)
            low = result[0]         
        if key == "aqi":
            aqi = winfo['aqi']
        if key == "fx":
            fx = winfo['fx']
        if key == "fl":
            fl = winfo['fl']
        if key == "type":
            type = winfo['type']
        if key == "notice":
            notice = winfo['notice']

      
  
def abouttoday(weatherdata):
    wendu = tonumber(weatherdata['wendu'])
    if wendu > 40:
        print('热死人')
    elif wendu > 35:
        print('高温')
    elif wendu > 30:   
        print('热')
    elif wendu > 20:   
        print('适宜')
    elif wendu > 10:
    
#合肥天气
link = 'http://t.weather.sojson.com/api/weather/city/101220101'


def getweatherinfo():
    redata = getrequest(link)
    timesinfo = redata['time']
    cityInfo = redata['cityInfo']
    weatherdata = redata['data']
    print(weatherdata)
    
    #今天
    shidu = weatherdata['shidu']        
    pm25 = weatherdata['pm25']
    quality = weatherdata['quality']
    wendu = weatherdata['wendu']
    ganmao = weatherdata['ganmao']

    #昨天
    yesterday = weatherdata['yesterday']
    #未来几天
    forecast = weatherdata['forecast']

    getwinfo(yesterday)
    
    #今天温度怎么样
    
    #明天会
    

getweatherinfo()


    
    
    