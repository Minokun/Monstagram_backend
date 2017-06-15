## Monstagram-backend
### 本项目是Monstagram网站的后台服务，包括整个接口，服务框架是python的django

### 接口文档：

##目录
>获取个性服务服务商列表
>获取个性服务商详情
>获取问卷诊断列表
>获取问卷诊断结果



## **`获取个性服务服务商列表`**
##### **接口调用请求说明**
>HTTP请求方式：POST
>请求数据格式：Content Type:application/x-www-form-urlencoded
>URL：[//example.com/service/providerv/list](www.api.com/index.php)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----                               |     
|offset|N|Int  |页数            
     

##### **返回说明**
正常时的返回JSON数据包：
```javascript
{
    "providerList": [
        {
            "id": "2",
            "logo": "personalize/01eb9d2c38fe933e60e7d013c0a4462d.png",
            "name": "微聚元设计师",
            "introduction": "微聚元设计工作室",
        }]
    "offset": 1,
   
}
```
|参数名|数据类型|说明                              |
|:-----   |:------|:-----------------------------   |
|id|int|ID                      |
|name|string |公司或团队名称                |
|logo|string |logo                    |
|introduction|string |简介|
|offset|int|开始的位置，从1开始



