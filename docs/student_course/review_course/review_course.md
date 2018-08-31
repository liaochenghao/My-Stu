### 获取学生审课方案课程

**请求地址**:
```
    GET     /api/v1/review_course/{id}/
```

**请求参数**:
```
{
    id
    不加id参数返回所有学生审课方案课程信息
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
                "remark": "6",
                "review": 2,
                "status": true,
                "project": 1,
                "review_certificate": "5",
                "modified_time": "2018-08-08T10:29:40Z"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```