#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

data = readJSON.读JSON文件("data.json")
名人名言 = data["famous"] # a 代表前面垫话，b 代表后面垫话
前面垫话 = data["before"] # 在名人名言前面弄点废话
后面垫话 = data['after']  # 在名人名言后面弄点废话
废话 = data['bosh'] # 代表文章主要废话来源
论点 = data['idea'] # 
结尾句 = data['ending'] #
引入用的后面垫话 = data['after-for-entry'] 
第一个分论点引入 = data['idea-entry-first']
更多分论点引入 = data['idea-entry-after']
观点总结 = data['ending']


重复度 = 1

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)
下一个论点 = 洗牌遍历(论点)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 引入用的名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(引入用的后面垫话) )
    return xx

def 主题段():
    xx = "\u3000\u3000" # 段前两个全角空格
    xx += 引入用的名言()
    骰子 = random.randint(0,100)
    while True:
        if 骰子 < 5:
            xx += "\r\n"
            return xx
        elif 骰子 < 20:
            xx += 来点名人名言()
        else:
            xx += next(下一句废话)
        骰子 = random.randint(0,100)

def 第一个分论点段():
    xx = "\u3000\u3000" # 段前两个全角空格
    段论点 = next(下一个论点)
    xx += random.choice(第一个分论点引入)
    骰子 = random.randint(0,100)
    while True:
        if 骰子 < 5:
            xx += random.choice(观点总结)
            xx += "\r\n"
            xx = xx.replace("t", 段论点)
            return xx
        elif 骰子 < 20:
            xx += 来点名人名言()
        else:
            xx += next(下一句废话)
        骰子 = random.randint(0,100)


def 更多的分论点段():
    xx = "\u3000\u3000" # 段前两个全角空格
    段论点 = next(下一个论点)
    xx += random.choice(更多分论点引入)
    骰子 = random.randint(0,100)
    while True:
        if 骰子 < 5:
            xx += random.choice(观点总结)
            xx += "\r\n"
            xx = xx.replace("t", 段论点)
            return xx
        elif 骰子 < 10:
            xx += 来点名人名言()
        else:
            xx += next(下一句废话)
        骰子 = random.randint(0,100)


def 结尾段():
    xx = "\u3000\u3000" # 段前两个全角空格
    xx += 来点名人名言()
    骰子 = random.randint(0,100)
    while True:
        if 骰子 < 5:
            xx += random.choice(观点总结)
            xx += "\r\n"
            xx = xx.replace("t", "无可奈何的")
            return xx
        elif 骰子 < 20:
            xx += 来点名人名言()
        else:
            xx += next(下一句废话)
        骰子 = random.randint(0,100)


if __name__ == "__main__":
    xx = input("请输入文章主题:")
    if xx == "":
        xx = "学生会退会"
    论文 = str()
    论文 += 主题段()
    # 添加论点段
    论文 += 第一个分论点段()
    while ( len(论文) < 6000 ) :
        论文 += 更多的分论点段()
    论文 += 结尾段()
    论文 = 论文.replace("x",xx)
    print(论文)

