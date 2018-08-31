### 修改学生审课方案课程

**请求地址**:
```
    PUT    /api/v1/review_course/{id}/
```

**请求参数**:
```
{
         "course_code": str 课程代码 ,
        "name": str 课程名称 ,
        "remark": str 备注,
        "review": int 审课方案id ,
        "status": bool 审课状态 default=False,
        "project": int 项目id ,
        "review_certificate": str 审课凭据,
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 2,
        "course_code": "110",
        "name": "3",
        "remark": "6",
        "review": 2,
        "status": true,
        "project": 1,
        "review_certificate": "5",
        "modified_time": "2018-08-08T07:32:08.053000Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```