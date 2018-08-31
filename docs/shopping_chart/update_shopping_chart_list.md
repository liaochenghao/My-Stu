###  修改购物车

**请求地址**:
```
    PUT  /shopping_chart/update_charts/
```

**请求参数**:
```
        [{"chart_id":1,"course_num":2},{"chart_id":2,"course_num":3}]
        
        chart_id        购物车ID
        course_num      课程数量
```

**成功返回**：
```

{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 1,
        "project": {
            "id": 1,
            "campus": 2,
            "name": "北京一期项目",
            "start_date": "2018-08-11",
            "end_date": "2018-08-11",
            "address": "北京大学",
            "info": "北京大学一期项目",
            "create_time": "2018-08-11T09:48:13Z",
            "apply_fee": 2000.0,
            "course_num": 3,
            "is_active": true,
            "campus_name": "北京"
        },
        "course_num": 1
    },
    "field_name": ""
}
```

**失败返回**：
```

```