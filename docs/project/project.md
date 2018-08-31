### 获取项目

**请求地址**:
```
    GET     /api/v1/project/{id}
```

**请求参数**:
```
{
    id
    不加id参数返回所有项目信息
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 1,
        "campus": 1,
        "name": "北京一期项目",
        "start_date": "2018-08-06",
        "end_date": "2018-08-24",
        "address": "北京大学",
        "info": "北京一期项目",
        "create_time": "2018-08-06T11:07:07Z",
        "apply_fee": 2000,
        "course_num": 2,
        "is_active": true,
        "campus_name": "武汉"
    },
    "field_name": ""
}
```

**失败返回**：
```

```