###  获取购物车项目

**请求地址**:
```
    GET  /api/v1/shopping_chart/get_user_project/
```

**请求参数**:
```
    student_id  int
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 1,
        "order": 10,
        "project1": {
            "id": 1,
            "campus": 2,
            "name": "北京一期项目",
            "start_date": "2018-08-11",
            "end_date": "2018-08-11",
            "address": "北京大学",
            "info": "北京大学一期项目",
            "create_time": "2018-08-11T09:48:13",
            "apply_fee": 2000.0,
            "course_num": 3,
            "is_active": true,
            "campus_name": "北京",
            "course_number": 1
        },
        "course_num1": 1,
        "project2": {
            "id": 2,
            "campus": 2,
            "name": "武汉一期项目",
            "start_date": "2018-08-10",
            "end_date": "2018-08-15",
            "address": "武汉科技大学",
            "info": "武汉一期项目",
            "create_time": "2018-08-11T09:49:11",
            "apply_fee": 2000.0,
            "course_num": 3,
            "is_active": true,
            "campus_name": "武汉",
            "course_number": 2
        },
        "course_num2": 2,
        "project3": null,
        "course_num3": null,
        "project4": null,
        "course_num4": null,
        "all_amount": 111.0
    },
    "field_name": ""
}
```

**失败返回**：
```

```