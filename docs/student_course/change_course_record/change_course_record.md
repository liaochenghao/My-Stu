### 获取学生调课记录

**请求地址**:
```
    GET     /api/v1/change_course_record/{id}/
```

**请求参数**:
```
{
    id
    不加id参数返回所有学生调课记录信息
}
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
                "student": 2,
                "previous_course_code": "2",
                "aim_course_code": "3",
                "student_server_id": "4",
                "create_time": "2018-08-08T10:39:34Z"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```