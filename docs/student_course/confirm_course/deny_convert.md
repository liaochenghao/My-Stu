### 确认转学分成功

**请求地址**:
```
    GET     /api/v1/confirm_course/deny_convert/
```

**请求参数**:
```
{
         "course_code": str 课程代码 ,
         "student_id": 学生id int ,
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