# -*- coding: utf-8 -*-
import urllib
import urllib2
import re



#def getvideo(page):#封装成一个方法便于调用

req = urllib2.Request('http://www.budejie.com/video/')#获取爬虫地址
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) %s/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36" )#键值对头部请求
html=urllib2.urlopen(req).read()#读取爬虫地址
reg =r'data-mp4="(.*?)"'#使用正则式方式获取方式
re.findall(reg,html)#进行匹配
for i in re.findall(reg,html):#便利地址
            filename = i.split("/")[-1]#分割，获取倒数不相同的文件名
            print('download......%s' %filename)
            urllib.urlretrieve(i,"mp4/%s" %filename)#进行下载
#for i in range(1,5):#下载1-5页，去头不取尾
#    pass