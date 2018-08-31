### 根据学生id获取学服老师及确认课程时间

**请求地址**:
```
    GET     /api/v1/confirm_course/get_server_time/
```

**请求参数**:
```
{
      student_id 学生id int
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