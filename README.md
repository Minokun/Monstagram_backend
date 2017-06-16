## Monstagram-backend
### 本项目是Monstagram网站的后台服务，包括整个接口，服务框架是python的django

### 接口文档：

## 目录
>首页作品展示列表
>登录
>获取access_token
>注册
>作品发布
>退出登录



## **`首页作品展示列表`**
##### **接口调用请求说明**
>HTTP请求方式：POST
>请求数据格式：Content Type:application/x-www-form-urlencoded
>URL：[//example.com/show_list](localhost/show_list)

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
|id|int|作品id|
|nickname|string | 用户昵称 |
|time| string | 发布时间 |
|img_url|string |图片地址|
|title|string |图片标题|
|comment|array|评论列表|



