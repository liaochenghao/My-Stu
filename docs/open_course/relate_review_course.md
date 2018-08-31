### 查看关联审课课程

**请求地址**:
```
    GET     /api/v1/project_course/relate_review_course/
```

**请求参数**:
  
```
    course_id 课程id int (course)
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "id": 1,
            "project__campus__name": "上海",
            "course_name": "金融",
            "course__course_code": "11",
            "select_course_num": 1
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```