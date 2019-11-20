/*
* @Author: Admin
* @Date:   2019-11-01 16:52:52
* @Last Modified by:   Admin
* @Last Modified time: 2019-11-05 01:34:26
*/

const fs = require("fs")
/**
 * 将JSON文件转化为对象
 * @type {String}
 * @return {Object} JSON文件转换后的数据对象
 */
function 读JSON文件(fileName=''){
    var strList = fileName.split(".");
    var string;
    if(strList[strList.length-1].toLowerCase()=="json"){
        string = fs.readFileSync(fileName);
    }
    return JSON.parse(string.toString())

}
module.exports={
    读JSON文件:读JSON文件
}