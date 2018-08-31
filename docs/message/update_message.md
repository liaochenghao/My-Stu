### 查询当前学生消息列表

**请求地址**:
```
    PATCH     /api/v1/message/student/{message_id}/
```

**请求参数**:
```
{
    message_id:  str 非空
    status: 1
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 1,
        "student": 1,
        "message": "fewfw",
        "create_time": "2018-08-23T11:50:12",
        "status": true,
        "update_time": "2018-08-23T12:01:02.762042"
    },
    "field_name": ""
}
```

**失败返回**：
```

```