### 查询当前学生消息列表

**请求地址**:
```
    POST     /api/v1/message/student/
```

**请求参数**:
```
{
    "student":2,
    "message":"456789"
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 4,
        "student": 2,
        "message": "fewfw",
        "create_time": "2018-08-23T11:59:36.652684",
        "status": false,
        "update_time": "2018-08-23T11:59:36.652684"
    },
    "field_name": ""
}
```

**失败返回**：
```

```