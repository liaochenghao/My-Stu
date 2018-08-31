### 根据学生id获取审课-项目信息

**请求地址**:
```
    GET     /api/v1/confirm_course/review_project/{student_id}
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
            "course_name": "线性代数", (课程别名)
            "course_code": "22",
            "school": "深圳大学",
            "course": 2,
            "course__name": "数学7894", (课程原名)
            "project": [
                {
                    "project": 2,
                    "project__name": "武汉一期项目",
                    "course": 2,
                    "project__course_num": 3
                },
                {
                    "project": 1,
                    "project__name": "北京一期项目",
                    "course": 2,
                    "project__course_num": 3
                }
            ]
        },
        {
            "course_name": "市场营销",
            "course_code": "111",
            "school": "杭州大学",
            "course": 11,
            "course__name": "市场营销",
            "project": []
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```