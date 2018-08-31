### 获取课程

**请求地址**:
```
    GET     /api/v1/record/
```

**请求参数**:
```
id
不加id参数返回所有渠道记录信息
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "user_id": 1,
                "channel_id": 2,
                "create_time": "2018-08-06T19:27:11Z"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```