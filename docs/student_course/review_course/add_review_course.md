### 添加学生审课方案课程

**请求地址**:
```
    POST     /api/v1/review_course/add_review_course/
```

**请求参数**:
```
{       参数 course:

        "student_id" : int 学生id 
        "course_name": str 课程名称
        "school": str 主办大学 
        "course_id": int 课程id 
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": "创建成功！",
    "field_name": ""
}
```

**失败返回**：
```

```