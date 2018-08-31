### 查看审课凭据

**请求地址**:
```
    GET    /api/v1/review_course/get_certificate/
```

**请求参数**:
```
{
         "course_code": str 课程代码 ,
        "student_id": int 学生id ,
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "review_certificate": "https://cp1.lxhelper.com/media/images/certificate/4aafee39-ef8f-4f8f-860c-6ef8aceefda8.jpg"
    },
    "field_name": ""
}
```

**失败返回**：
```

```