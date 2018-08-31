### 添加学生审课方案

**请求地址**:
```
    PUT    /api/v1/review/{id}/
```

**请求参数**:
```
{
        "student": int 学生id ,
        "student_server_id": str 学服id ,
        "remark":  str 备注 ,
        "school": str 学校  ,
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 4,
        "student": 2,
        "student_server_id": "5",
        "remark": "7",
        "school": "6",
        "create_time": "2018-08-08T03:15:35.629700Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```