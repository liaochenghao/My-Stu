### 根据课程id搜索项目

**请求地址**:
```
    GET     /api/v1/project_course/get_project/
```

**请求参数**:
```
{
       "course_id":课程id int
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "project": 2,
            "project__name": "武汉一期项目"
        },
        {
            "project": 1,
            "project__name": "北京一期项目"
        },
        {
            "project": 4,
            "project__name": "上海一期项目"
        },
        {
            "project": 4,
            "project__name": "上海一期项目"
        },
        {
            "project": 5,
            "project__name": "一期"
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```