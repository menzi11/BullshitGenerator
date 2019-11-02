#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

data = readJSON.读JSON文件("data.json")
名人名言 = data["famous"] # a 代表前面垫话，b代表后面垫话
前面垫话 = data["before"] # 在名人名言前面弄点废话
后面垫话 = data["after"]  # 在名人名言后面弄点废话
废话 = data["bosh"] # 代表文章主要废话来源
句内点号 = data["nonstop"] # 要替换的结尾标点
句末点号 = data["stop"] # 要保留的结尾标点

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句名人名言 = 洗牌遍历(名人名言)
下一句废话 = 洗牌遍历(废话)

def 来点名人名言(文章主题):
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace("a", random.choice(前面垫话))
    xx = xx.replace("b", random.choice(后面垫话))
    xx = xx.replace("x", 文章主题)
    return xx

def 来点废话(文章主题):
    global 下一句废话
    xx = next(下一句废话)
    xx = xx.replace("x", 文章主题)
    return xx

def 另起一段(段落结尾):
    xx = 段落结尾
    xx += "\r\n"
    xx += "　　" # 两个全角空格
    return xx

if __name__ == "__main__":
    xx = input("请输入文章主题（多个以空格分隔）：").split(" ")
    limit = input("请输入每篇大致字数（最小值100，过小则设为最小值，空则默认6000）：")
    if len(limit) == 0:
        limit = 6000
    elif int(limit) < 100:
        limit = 100
    else:
        limit = int(limit)
    for x in xx:
        print(x + "：")
        tmp = "　　" # 两个全角空格
        while len(tmp) < limit:
            分支 = random.randint(0,100)
            if 分支 < 5:
                if len(tmp) == 0 or tmp[-1] == "　": pass
                elif tmp[-1] in 句内点号:
                    tmp = tmp[:-1]
                    tmp += 另起一段("。")
                elif tmp[-1] in 句末点号:
                    tmp += 另起一段("")
                else:
                    tmp += 另起一段("。")
            elif 分支 < 20:
                tmp += 来点名人名言(x)
            else:
                tmp += 来点废话(x)
        if len(tmp) == 0 or tmp[-1] == "　": pass
        elif tmp[-1] in 句内点号:
            tmp = tmp[:-1] + "。"
        elif tmp[-1] in 句末点号: pass
        else:
            tmp += "。"
        print(tmp)
