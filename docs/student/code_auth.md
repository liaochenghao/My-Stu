### 通过code认证接口

**请求地址**:
```
    GET    /api/v1/student/info/authorize/
```

**请求参数**:
```
     {
        "code": "XXXXXX"       
     }
```

**成功返回**：
```
{
    "code": null,
    "msg": "请求成功",
    "data": {
        "user_id": "123"       
        "student_status": "NEW"       
    },
    "field_name": ""
}
```

**失败返回**：
```

```