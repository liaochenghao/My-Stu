### 添加确认课程

**请求地址**:
```
    POST     /api/v1/confirm_course/add_course/
```

**请求参数**:
```
{
        "course_code": str 课程代码 
        "course_name":  str 课程名称
        "student_id": int 学生id 
        "project_id":  int 项目id
        "course_id":  int 课程id
        "school": str 主办大学
        "change_type" str 调课类别
        "extra"  str 备注
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 2,
        "course_code": "120",
        "name": "4",
        "remark": "8",
        "student": 2,
        "create_time": "2018-08-08T07:47:59.269000Z",
        "project_course": 1,
        "score": "99",
        "modified_time": "2018-08-08T07:47:59.269000Z",
        "status": true,
        "score_enter_time": "2018-08-08T10:36:51Z",
        "grade": "5",
        "convert_credit_status": true,
        "image": null
    },
    "field_name": ""
}
```

**失败返回**：
```

```