### 新增用户

**请求地址**:
```
    POST     /api/v1/user_info/
```

**请求参数**:
```
{
        "username": "bobowang1112",
        "role_id": 1,
        "role_name": 1,
        "name": "",
        "email": "",
        "phone": "",
        "sex": false,
        "department_id": 1,
        "department_name": 1,
        "qr_code":  图片,
        "leader_id": 1,
        "leader_name": "fewf",
        "wechat":"15926",
        "is_leader": true
    }
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 8,
        "username": "bobowang1112",
        "role_id": 1,
        "name": "",
        "email": "",
        "phone": "",
        "sex": false,
        "department_id": 1,
        "active": false,
        "qr_code": "http://127.0.0.1:8000/media/images/user_qrcode/sign_WwSPgEj.png",
        "create_time": "2018-08-08T07:39:33.979240Z",
        "update_time": "2018-08-08T07:39:33.980236Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```