### 查询当前学生消息列表

**请求地址**:
```
    GET     /api/v1/message/student/?student={student_id}
```

**请求参数**:
```
{
    student_id:  str 非空
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "student": 1,
                "message": "dfw",
                "create_time": "2018-08-23T11:50:12",
                "status": true,
                "type": 0,
                "update_time": "2018-08-23T11:51:58"
            },
            {
                "id": 2,
                "student": 1,
                "message": "456789",
                "create_time": "2018-08-23T11:56:43",
                "status": false,
                "type": 0,
                "update_time": "2018-08-23T11:56:43"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```