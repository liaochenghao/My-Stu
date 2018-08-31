### 获取课程

**请求地址**:
```
    GET     /api/v1/course/{id}
```

**请求参数**:
```
{
    id
    不加id参数返回所有课程信息
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
                "course_code": "2",
                "name": "葵花宝典",
                "extra": null,
                "credit": 2,
                "create_time": "2018-08-06T10:47:52Z"
            },
            {
                "id": 2,
                "course_code": "45",
                "name": "九阴真经",
                "extra": null,
                "credit": 2,
                "create_time": "2018-08-06T10:49:20Z"
            },
            {
                "id": 3,
                "course_code": "56",
                "name": "碧海潮生曲",
                "extra": null,
                "credit": 3,
                "create_time": "2018-08-06T10:52:31Z"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```