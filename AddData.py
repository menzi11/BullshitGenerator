# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2019-11-01 16:52:34
# @Last Modified by:   Liu Tongyang
# @Last Modified time: 11月14日16:37:00
import json

# 读取待添加数据
with open('AddData.txt', 'r', encoding="utf-8") as f:
    Add_Data = []
    for temp_data in f.readlines():
        Add_Data.append(temp_data.strip())
    
# 把要字段改为你要添加的那个部分，目前待选有：famous bosh after before
with open('data.json', 'r', encoding='utf-8') as fi:
    ori_data = json.loads(fi.read())
    ori_data['famous'].extend(Add_Data)

json_str = json.dumps(ori_data, indent=4, ensure_ascii=False)

with open('data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)