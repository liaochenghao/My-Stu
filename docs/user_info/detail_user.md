### 查询用户详情

**请求地址**:
```
    GET     /api/v1/user_info/{user_id}
```

**请求参数**:
```
{
    
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 1,
        "username": "bobo",
        "role_id": 1,
        "name": "波波",
        "email": "09879654@qq.com",
        "phone": "15926215673",
        "sex": true,
        "department_id": 1,
        "active": true,
        "qr_code": "fewf",
        "create_time": "2018-08-06T11:09:39Z",
        "update_time": "2018-08-06T11:09:41Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```