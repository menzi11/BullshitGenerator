/*
* @Author: Admin
* @Date:   2019-11-01 16:52:52
* @Last Modified by:   jingyuexing
* @Last Modified time: 2019-11-01 17:36:11
*/

const fs = require("fs")
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