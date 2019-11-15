# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2019-11-01 16:52:34
# @Last Modified by:   Admin
# @Last Modified time: 2019-11-01 18:18:14
def 读JSON文件(fileName=""):
    import json
    if fileName!='':
        strList = fileName.split(".")
        if strList[len(strList)-1].lower() == "json":
            with open(fileName,mode='r',encoding="utf-8") as file:
                return json.loads(file.read())
