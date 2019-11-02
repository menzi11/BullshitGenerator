# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2019-11-02 19:10:25
# @Last Modified by:   Admin
# @Last Modified time: 2019-11-02 19:10:42

#对名人名言去重
def 去重(file):
    import readJSON
    import re
    temp  = readJSON.读JSON文件(file)['famous']
    for x in temp:
       for n in temp:
           m=0
           if x == n:
               temp.pop(m)
               m=m+1
    return temp
if __name__ == "__main__":
    data = 去重("famous.json")
    print(data)