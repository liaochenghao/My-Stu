### 修改确认课程

**请求地址**:
```
    PATCH     /api/v1/confirm_course/{id}/
```

**请求参数**:
```
{
        "course_code": str 课程代码 ,
        "name":  str 课程名称,
        "remark":  str 备注,
        "student": int 学生id ,
        "project_course":  int 项目课程id ,
        "score":  str 成绩分数 ,
        "status": bool 确认状态 default=False,
        "score_enter_time": datetime 成绩录入时间,
        "grade":  str 等级 ,
        "convert_credit_status": bool 转学分状态 default=False,
        "image": file 转学分图片 
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 2,
        "course_code": "121",
        "name": "4",
        "remark": "8",
        "student": 2,
        "create_time": "2018-08-08T07:47:59.269000Z",
        "project_course": 1,
        "score": "99",
        "modified_time": "2018-08-08T07:58:34.586000Z",
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