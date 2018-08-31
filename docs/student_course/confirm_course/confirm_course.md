### 获取确认课程

**请求地址**:
```
    GET     /api/v1/confirm_course/{id}/
```

**请求参数**:
```
{
    id
    不加id参数返回所有确认课程信息
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
                "course_code": "2",
                "name": "3",
                "remark": "7",
                "student": 1,
                "create_time": "2018-08-08T10:36:45Z",
                "project_course": 1,
                "score": "8",
                "modified_time": "2018-08-08T10:36:49Z",
                "status": true,
                "score_enter_time": "2018-08-08T10:36:51Z",
                "grade": "9",
                "convert_credit_status": true,
                "image": "http://127.0.0.1:9999/media/6"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```