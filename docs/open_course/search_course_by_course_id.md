### 根据课程id搜索开课列表

**请求地址**:
```
    GET     /api/v1/project_course/
```

**请求参数**:
  
```
    course 课程id 
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "modified_time": "2018-08-11T09:51:31",
                "create_time": "2018-08-11T09:51:16",
                "status": true,
                "professor": "金立群",
                "start_time": "2018-08-11T09:51:11",
                "end_time": "2018-08-11T09:51:13",
                "address": "上海财经大学",
                "course": 1,
                "project": 4,
                "course_name": "金融",
                "max_select_num": 20,
                "campus_id": 1,
                "select_course_num": 0,
                "campus_name": "上海",
                "project_name": "重庆"
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```