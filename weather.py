# -*- coding: utf-8 -*-
"""
Created on Thu May  6 17:23:44 2021

@author: Administrator
"""

import requests
import re


def weather(c):
    
    
    #获取时间
    hea = {'User-Agent': 'Mozilla/5.0'}
    url_time = r'http://time1909.beijing-time.org/time.asp'
    r_time = requests.get(url_time, headers = hea)
    if r_time.status_code == 200:
        result_time = r_time.text
        data_time = result_time.split(';')
    regex = r'\d+' #匹配连续数字
    x = [1,2,3,5,6,7] 
    y = ['年','月','日','时','分','秒']
    t = []
    for i,j in zip(x,y):
        m = re.findall(regex , data_time[i])
        t.append(m[0]+j)

    #获取天气信息
    url = r'http://wthrcdn.etouch.cn/weather_mini?city='+c
    r = requests.get(url)
    r.encoding = 'utf8'
    result = r.json()
    w_f = result['data']['forecast']
    w_f.insert(0,result['data']['yesterday'])
    ps = result['data']['ganmao']
    wendu = result['data']['wendu']
    
    #拼合时间
    t_date = []
    for d in range(len(result['data']['forecast'])):
        t_d = t[0]+t[1]+result['data']['forecast'][d]['date']
        t_date.append(t_d)

    return w_f,ps,wendu,t_date


while True:
    city = input("天气查询v1.0\n请输入要查询天气的城市，退出请输入：e\n")
    if city == "e":
        break
    else:
        data,s_data,wen,time_data = weather(city)
        regex = r'[\d\u4E00-\u9FA5]'
        m = re.findall(regex , data[1]['fengli'])
        f = m[0]+m[1]
        print('%s%s地区，%s%s，%s%s'%(time_data[1],city,data[1]['high'],data[1]['low'],data[1]['fengxiang'],f))
        print('%s\n'%(s_data))
        
        
        
        
        
        
        # print('%s此时的气温为%s度'%(city,wen))
