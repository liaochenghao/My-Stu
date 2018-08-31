### 根据学生id获取课程调整记录

**请求地址**:
```
    GET     /api/v1/change_course_record/get_change_record/{student_id}
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
            "student_server": 1,
            "course_code": "11", (课程代码)
            "course_name": "金融学", (课程名称)
            "project": "重庆大学一期项目",(关联项目名称)
            "course": "金融学123415646", (关联课程原名)
            "school": "重庆大学", (主办大学)
            "modified_time": "2018-08-28T18:39:16.161000",
            "change_type": "加课",
            "extra": "换了一门课,加5千"
        },
        {
            "student_server": 1,
            "course_code": "11",
            "course_name": "金融学",
            "project": "重庆大学一期项目",
            "course": "金融学123415646",
            "school": "重庆大学",
            "modified_time": "2018-08-28T18:40:24.032000",
            "change_type": "加课",
            "extra": "换了一门课,加5千"
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```