### 确认成绩

**请求地址**:
```
    GET     /api/v1/confirm_course/confirm_performance/
```

**请求参数**:
```
{
    course_code 课程代码 str,
    course_name 课程名称 str,
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "status": true,
        "modified_time": "2018-08-22T11:08:39"
    },
    "field_name": ""
}
```
**失败返回**：
```

```