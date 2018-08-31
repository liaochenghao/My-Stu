### 添加项目

**请求地址**:
```
    POST     /api/v1/project/
```

**请求参数**:
```
    campus 校区id int 非空
    campus_name 关联校区名称 str 非空    
    project_name 项目名称 str 非空
    start_date 开始时间 datetime 非空
    end_date 结束时间 datetime 非空
    address 项目地点 str
    info 项目描述 str
    apply_fee 申请费 int 
    course_num 课程数 int 非空
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 2,
        "campus": 2,
        "project_name": "武汉一期项目",
        "start_date": "2018-08-10",
        "end_date": "2018-08-15",
        "address": "武汉大学",
        "info": "武汉一期项目",
        "create_time": "2018-08-10T03:22:00.159400Z",
        "apply_fee": 2000,
        "course_num": 3,
        "is_active": false,
        "campus_name": "武汉"
    },
    "field_name": ""
}
```

**失败返回**：
```

```