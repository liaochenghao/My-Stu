### 添加学生审课方案

**请求地址**:
```
    POST     /api/v1/change_course_record/add_change/
```

**请求参数**:
```
{       
        student_id 学生id
        course_name 课程名称
        course_code 课程代码
        school 主办大学
        course 课程关联名称
        project 项目关联名称
        change_type 调整类别
        extra 备注
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 4,
        "student": 1,
        "student_server": 1,
        "course_code": "11",
        "course_name": "金融学",
        "create_time": "2018-08-28T18:40:24.032000",
        "project": "重庆大学一期项目",
        "school": "重庆大学",
        "course": "金融学123415646",
        "modified_time": "2018-08-28T18:40:24.032000",
        "change_type": "加课",
        "extra": "换了一门课,加5千"
    },
    "field_name": ""
}

```

**失败返回**：
```

```