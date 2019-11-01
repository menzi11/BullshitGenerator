#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON
data = readJSON.读JSON文件("data.json")
名人名言 = data["famous"]
前面垫话 = data["before"]
后面垫话 = data['after']
废话 = data['bosh']
xx = data['title']
def 来点名人名言():
    xx = 名人名言[random.randint(0,len(名人名言)-1)]
    xx = xx.replace(  "a",前面垫话[random.randint(0,len(前面垫话)-1)] )
    xx = xx.replace(  "b",后面垫话[random.randint(0,len(后面垫话)-1)] )
    return xx

def 另起一段():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx


for x in xx:
    tmp = str()
    while ( len(tmp) < 6000 ) :
        分支 = random.randint(0,100)
        if 分支 < 5:
            tmp += 另起一段()
        elif 分支 < 20 :
            tmp += 来点名人名言()
        else:
            tmp += 废话[random.randint(0,len(废话)-1)]
    tmp = tmp.replace("x",xx)
    print(tmp)
