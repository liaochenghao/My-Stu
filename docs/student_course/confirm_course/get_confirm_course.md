### 根据学生id获取确认课程

**请求地址**:
```
    GET     /api/v1/confirm_course/get_confirm_course/{student_id}
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
            "id": 1,
            "course_code": "11",
            "course_name": "大众文化",
            "school": "重庆大学",
            "project_course__course__name": "大众文化",
            "project_course__address": "重庆大学",
            "project_course__start_time": "2018-08-11",
            "project_course__project__name": "重庆一期项目"
        }
    ],
    "field_name": ""

```

**失败返回**：
```

```