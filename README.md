## Monstagram-backend
### 本项目是Monstagram网站的后台服务，包括整个接口，服务框架是python的django

### 接口文档：

## 目录
>首页作品展示列表
>作品发布
>注册
>用户信息修改
>登录
>退出登录



## **`首页作品展示列表`**
##### **接口调用请求说明**
>HTTP请求方式：get
>请求数据格式：Content Type:application/x-www-form-urlencoded
>URL：[//example.com/resource_list](localhost/resource_list)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|offset|N|Int  |页数            
     

##### **返回说明**
正常时的返回JSON数据包：
```javascript
[
    {
        "id": 1,
        "user_id": 1,
        "title": "哟哟哟",
        "img_url": "http://www.baidu.com",
        "created_at": 143234234,
        "status": 1
    }
]
```
|参数名|数据类型|说明                              |
|:-----   |:------|:-----------------------------   |
|id|int|作品id|
|user_id|int| 用户id |
|title| string | 标题 |
|img_url|string |图片地址|
|created_at|int |创建时间|
|comment|array|评论列表|



