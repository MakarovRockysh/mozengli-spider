# -*- coding: utf-8 -*-
import base64
import re

thunderPrefix = "AA";
thunderPosix = "ZZ";
thunderTitle = "thunder://";

def ThunderEncode(url):
    url = url[len(thunderTitle):]
    url = url.encode("utf-8")
    url = base64.b64decode(url)
    url = thunderTitle + thunderPrefix + url + thunderPosix
    return url

if __name__ == '__main__':
    url = "ftp://ygdy8:ygdy8@yg72.dydytt.net:8245/阳光电影www.ygdy8.com.厕所英雄.HD.720p.国印双语中字.mkv"
    ThunderEncode(url)