### 确认审课失败

**请求地址**:
```
    GET    /api/v1/review_course/deny_review_course/
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
    "data": "操作成功!",
    "field_name": ""
}
```

**失败返回**：
```

```