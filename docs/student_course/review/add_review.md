### 添加学生审课方案

**请求地址**:
```
    POST     /api/v1/review/
```

**请求参数**:
```
{       
        "student": int 学生id 非空,
        "student_server_id": str 学服id 非空,
        "remark":  str 备注,
        "school": str 学校  ,
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 5,
        "student": 2,
        "student_server_id": "5",
        "remark": "7",
        "school": "6",
        "create_time": "2018-08-08T03:19:27.942700Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```