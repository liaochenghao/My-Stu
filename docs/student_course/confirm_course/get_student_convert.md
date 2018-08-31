### 根据学生id获取学分转换信息

**请求地址**:
```
    GET     /api/v1/confirm_course/get_student_convert/{student_id}
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
            "convert_status": "CONVERT_WAIT",
            "course_name": "大众文化",
            "school": null,
            "image": "images/convert/273bb3f7-4797-4767-933c-b03dbce54705.png",
            "recipient_number": null,
            "sending_date": null,
            "project_course__project__name": "重庆一期项目"
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```