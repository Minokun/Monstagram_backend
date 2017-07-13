## Monstagram-backend
### 本项目是Monstagram网站的后台服务，包括整个接口，服务框架是python的django

### 接口文档：

## 目录
>注册
>登录
>首页作品展示列表
>作品发布
>提交评论
>点赞
>取消点赞
>查询当前用户是否点赞


## **`注册`**
##### **接口调用请求说明**
>HTTP请求方式：post
>请求数据格式：Content Type:application/json
>URL：[//example.com/v1/user_list](localhost/v1/user_list)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|email|Y| str | 用户邮箱 |     
|password|Y|str|密码|
| nickname |Y| str | 昵称 | 
|prefix|Y| int| 电话区域 |
| phone | Y | int | 联系电话|

##### **返回说明**
正常时的返回JSON数据包：
```javascript
{
    "id": 3,
    "email": "2524231862@qq.com",
    "nickname": "蜘蛛侠",
    "prefix": 86,
    "phone": 13060029781,
    "created_at": 1498643575,
    "updated_at": 1498643575
}
```

## **`登录`**
##### **接口调用请求说明**
>HTTP请求方式：post
>请求数据格式：Content Type:application/json
>URL：[//example.com/v1/login](localhost/v1/login)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|email|Y| str | 用户邮箱 |     
|password|Y|str|密码|

##### **返回说明**
正常时的返回JSON数据包：
```javascript
{
    "status": 1,
    "message": "登录成功！",
    "data": {
        "user_id": 5,
        "nickname": "蜘蛛侠"
    }
}
```


## **`首页作品展示列表`**
##### **接口调用请求说明**
>HTTP请求方式：get
>请求数据格式：Content Type:application/json
>URL：[//example.com/v1/resource_list](localhost/v1/resource_list)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|offset|N|Int  |页数  |     

##### **返回说明**
正常时的返回JSON数据包：
```javascript
[
    {
        "id": 1,
        "user_id": 1,
        "nickname": "上帝",
        "title": "哇哈哈",
        "img_url": "http://www.baidu.com",
        "created_at": 145273623,
        "updated_at": 145283783,
        "time_diff": "20 时",
        "praise_num": 0,
        "comment": [
            {
                "user_id": 1,
                "content": "我很喜欢合格",
                "created_at": 147283746,
                "user": {
                    "email": "952718180@qq.com",
                    "nickname": "上帝",
                    "phone": 13060029781,
                    "created_at": 145273623
                }
            },
            {
                "user_id": 1,
                "content": "我好饿啊",
                "created_at": 147283746,
                "user": {
                    "email": "952718180@qq.com",
                    "nickname": "上帝",
                    "phone": 13060029781,
                    "created_at": 145273623
                }
            }
        ]
    },
    {
        "id": 2,
        "user_id": 2,
        "title": "哟哟",
        "img_url": "http://www.sasd.com",
        "created_at": 145273623,
        "updated_at": 145273623,
        "time_diff": "20 时",
        "praise_num": 0,
        "comment": []
    }
]
```
|参数名|数据类型|说明                              |
|:-----   |:------|:-----------------------------   |
|id|int|作品id|
|user_id|int| 用户id |
|nick_name|str| 用户昵称 |
|title| string | 标题 |
|img_url|string |图片地址|
|created_at|int |创建时间|
|updated_at|int |更新时间|
|time_diff|str | 时间距离 |
|praise_num|int | 点赞数|
|comment|  |评论列表|
|user_id|int|评论者的id|
|content|str|评论内容|
|created_at|int|评论创建时间|
|user|  |评论用户信息|
|comment|array|评论列表|
|email|str|用户邮件|
|nickname|str|昵称|
|phone|int|联系方式|
|created_at|int|用户创建时间|



## **`作品发布`**
##### **接口调用请求说明**
>HTTP请求方式：post
>请求数据格式：Content Type:application/json
>URL：[//example.com/v1/resource_list](localhost/v1/resource_list)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|user_id|Y|Int | 用户ID |     
| title |Y| str | 标题 | 
|img_url|Y| str | 图片地址 |

##### **返回说明**
正常时的返回JSON数据包：
```javascript
{
    "status":1,
    "pic_url": "http://localhost:8000/static/102438879.jpeg"
}

```
|参数名|数据类型|说明                              |
|:-----   |:------|:-----------------------------   |
|id|int|作品id|
|user_id|int| 用户id |
|title| string | 标题 |
|img_url|string |图片地址|
|created_at|int |创建时间|
|updated_at|int |更新时间|


## **`提交评论`**
##### **接口调用请求说明**
>HTTP请求方式：post
>请求数据格式：Content Type:application/json
>URL：[//example.com/v1/resource_list](localhost/v1/resource_list)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|user_id|Y|Int | 评论用户ID |     
|resources_id |Y| Int | 作品id | 
|content|Y| str | 评论内容 |

##### **返回说明**
正常时的返回JSON数据包：
```javascript
{
    "id": 5,
    "user_id": 5,
    "resources_id": 2,
    "content": "这是一个神奇的世界",
    "created_at": 1499321821
}

```
|参数名|数据类型|说明                              |
|:-----   |:------|:-----------------------------   |
|id|int|评论id|
|user_id|int| 用户id |
|resources_id| int| 作品id |
|created_at|int |创建时间|
|content|str | 评论内容 |


## **`点赞`**
##### **接口调用请求说明**
>HTTP请求方式：post
>请求数据格式：Content Type:application/json
>URL：[//example.com/v1/praise](localhost/v1/praise)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|user_id|Y|Int | 评论用户ID |     
|resources_id |Y| Int | 作品id | 

##### **返回说明**
正常时的返回JSON数据包：
```javascript
{
    "status": 1,
    "message": "操作成功！"
}

```
|参数名|数据类型|说明                              |
|:-----   |:------|:-----------------------------   |
|status|int|状态|
|message|int| 具体信息 |


## **`取消点赞`**
##### **接口调用请求说明**
>HTTP请求方式：post
>请求数据格式：Content Type:application/json
>URL：[//example.com/v1/praise_cancel](localhost/v1/praise_cancel)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|user_id|Y|Int | 评论用户ID |     
|resources_id |Y| Int | 作品id | 

##### **返回说明**
正常时的返回JSON数据包：
```javascript
{
    "status": 1,
    "message": "操作成功！"
}

```
|参数名|数据类型|说明                              |
|:-----   |:------|:-----------------------------   |
|status|int|状态|
|message|int| 具体信息 |



## **`查询当前用户是否点赞`**
##### **接口调用请求说明**
>HTTP请求方式：post
>请求数据格式：Content Type:application/json
>URL：[//example.com/v1/praise_check](localhost/v1/praise_chec)

##### **请求参数**
|参数名|必填|数据类型|说明|
|:-----  |:-------|:-----|-----|     
|user_id|Y|Int | 评论用户ID |     
|resources_id |Y| Int | 作品id | 

##### **返回说明**
正常时的返回JSON数据包：
```javascript
{
    "status": 1,
    "message": "已点赞！"
}

```
|参数名|数据类型|说明                              |
|:-----   |:------|:-----------------------------   |
|status|int|状态|
|message|int| 具体信息 |






