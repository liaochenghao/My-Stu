### 根据学生id获取审课方案

**请求地址**:
```
    GET     /api/v1/review/get_review/{student_id}
```

**请求参数**:
```
{
    student_id 学生id int
}
```


**成功返回**：
```
{
    "code": 400,
    "msg": "已有审课方案",
    "data": {},
    "field_name": ""
}
```

**失败返回**：
```

```