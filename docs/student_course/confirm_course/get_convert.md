### 查看用户转学分图片

**请求地址**:
```
    GET     /api/v1/confirm_course/get_convert/
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
        "image": "https://cp1.lxhelper.com/media/images/convert/3dd51a36-a447-4fc1-b4b4-8293dd77a602.jpg"
    },
    "field_name": ""
}
```

**失败返回**：
```

```