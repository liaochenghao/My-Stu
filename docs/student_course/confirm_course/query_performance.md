### 查询成绩

**请求地址**:
```
    GET     /api/v1/confirm_course/query_performance/{student_id}
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
    "data": [
        {
            "course_code": "11",
            "course_name": "大众文化",
            "score": 100,
            "grade": "D",
            "score_enter_time": "2018-08-11T13:52:33",
            "status": "SCORE_WAIT",
            "modified_time": "2018-08-11T13:54:24",
            "project_course__course__name": "大众文化",
            "project_course__project__name": "重庆一期项目",
            "project_course__project__campus_name": "重庆"
        }
    ],
    "field_name": ""
}

```

**失败返回**：
```

```