### 获取校区

**请求地址**:
```
    GET     /api/v1/campus/{id}
```

**请求参数**:
```
{
    id
    不加id参数返回所有校区信息
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "北京",
                "info": "北京校区",
                "create_time": "2018-08-06T10:38:25Z",
                "update_time": "2018-08-06T10:39:19Z"
            },
            {
                "id": 2,
                "name": "武汉",
                "info": "武汉校区",
                "create_time": "2018-08-06T10:40:10Z",
                "update_time": "2018-08-06T10:40:13Z"
            },
            {
                "id": 4,
                "name": "杭州",
                "info": "杭州校区",
                "create_time": "2018-08-06T03:36:16.779000Z",
                "update_time": "2018-08-06T03:57:34.456000Z"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```