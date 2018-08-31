### 获取学生调课记录

**请求地址**:
```
    PUT     /api/v1/change_course_record/{id}/
```

**请求参数**:
```
{
        "student": int 学生id ,
        "previous_course_code": str 原有课程编号,
        "aim_course_code": str 目标课程编号,
        "student_server_id": str 学服编号,
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 2,
        "student": 2,
        "previous_course_code": "6",
        "aim_course_code": "110",
        "student_server_id": "120",
        "create_time": "2018-08-08T08:03:35.991000Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```