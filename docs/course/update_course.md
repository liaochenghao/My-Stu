### 修改校区

**请求地址**:
```
    PUT     /api/v1/course/{id}/
```

**请求参数**:
```
    course_code 课程代码 str 
    course_name 课程名称 str   
    credit 学分 int 
    extra 备注信息 str
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 2,
        "course_code": "101",
        "course_name": "葵花宝典",
        "extra": "该课程3个学分",
        "credit": 3,
        "create_time": "2018-08-10T02:35:34.170400Z",
        "modified_time": "2018-08-10T02:35:34.170400Z"
    },
    "field_name": ""
}
```

**失败返回**：
```


**失败返回**：
```

```