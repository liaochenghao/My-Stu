### 获取学生审课方案

**请求地址**:
```
    GET     /api/v1/review/{id}/
```

**请求参数**:
```
{
    id
    不加id参数返回所有学生审课方案信息
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
                "student": 1,
                "student_server_id": "2",
                "remark": "4",
                "school": "3",
                "create_time": "2018-08-08T10:28:34Z"
            },
            {
                "id": 2,
                "student": 1,
                "student_server_id": "3",
                "remark": "6",
                "school": "5",
                "create_time": "2018-08-08T10:28:59Z"
            },
            {
                "id": 3,
                "student": 2,
                "student_server_id": "4",
                "remark": "7",
                "school": "6",
                "create_time": "2018-08-08T10:29:20Z"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```