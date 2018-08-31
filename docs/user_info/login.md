### 后台用户登录

**请求地址**:
```
    POST     /api/v1/user_info/login/
```

**请求参数**:
```
{
        "username": "bobowang1112",
        "password": "123",
    }
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "token": "XXXX.YYYY.ZZZZ,        
    },
    "field_name": ""
}
```

**失败返回**：
```

```