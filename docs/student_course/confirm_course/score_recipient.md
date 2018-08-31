### 录入学生成绩等级或快递信息

**请求地址**:
```
    PATCH     /api/v1/confirm_course/score_recipient/
```

**请求参数**:
```
{
        student_id 学生id 必填 int
        course_code 课程代码 必填 str
        score 分数 int
        grade 等级 str
        recipient_number 快递单号 str
        sending_date 快递发送日期 date
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "score": 98,
        "grade": "A",
        "recipient_number": null,
        "sending_date": null
    },
    "field_name": ""
}
```

**失败返回**：
```

```