# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2019-11-01 16:52:34
# @Last Modified by:   Admin
# @Last Modified time: 2019-11-05 01:35:47
def 读JSON文件(fileName=""):
    """读取`JSON`文件并将其转换为字典`dict`
    
    [description]
    
    Keyword Arguments:
        fileName {str} -- 文件名 (default: {""})
    
    Returns:
        dict -- 返回的字典
    """
    import json
    if fileName!='':
        strList = fileName.split(".")
        if strList[len(strList)-1].lower() == "json":
            with open(fileName,mode='r',encoding="utf-8") as file:
                return json.loads(file.read())
