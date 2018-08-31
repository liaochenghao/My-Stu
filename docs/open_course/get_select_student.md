### 获取开课列表选课学生名单

**请求地址**:
```
    GET     /api/v1/confirm_course/get_select_student/{project_course_id}
```

**请求参数**:
  
```
    project_course_id 项目课程关联id int
    page 页码 int
    page_size 每页条数 int
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "confirmcourse__student__id_number": "888888888888888888888",
            "confirmcourse__student__name": "qwe",
            "confirmcourse__student__cc": "1",
            "confirmcourse__student__cschool": "asd",
            "confirmcourse__student__server": null
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```