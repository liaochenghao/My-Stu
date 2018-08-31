### 根据学生id查询快递

**请求地址**:
```
    GET     /api/v1/confirm_course/get_recipient/{student_id}
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
            "project_course__course_name": "大众文化",
            "project_course__project__name": "重庆一期项目",
            "score": 0,
            "grade": "D",
            "recipient_number": "12345678",
            "sending_date": "2018-08-23",
            "convert_status": "NO_SEND"
        },
        {
            "course_code": "22",
            "project_course__course_name": "金融",
            "project_course__project__name": "上海一期项目",
            "score": 77,
            "grade": "D",
            "recipient_number": "456789",
            "sending_date": "2018-08-23",
            "convert_status": "SENT"
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```