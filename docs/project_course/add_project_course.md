### 添加项目

**请求地址**:
```
    POST     /api/v1/project_course/
```

**请求参数**:
```
    "professor": str 教授姓名 
    "start_time": date 上课开始时间 
    "end_time": date 上课结束时间 
    "address": str 上课地点 
    "course": int 课程id 
    "project": int 项目id 
    "course_name": str 课程别名 
    "max_select_num": int 最大选课人数 
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 5,
        "modified_time": "2018-08-11T06:34:03.728000Z",
        "create_time": "2018-08-11T06:34:03.728000Z",
        "status": true,
        "professor": "谭胜龙",
        "start_time": "2018-08-11T09:51:11Z",
        "end_time": "2018-08-11T09:51:13Z",
        "address": "北京大学",
        "course": 1,
        "project": 1,
        "course_name": "计算机",
        "max_select_num": 20
    },
    "field_name": ""
}
```

**失败返回**：
```

```