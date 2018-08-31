### 检查用户的菜单访问权限

**请求地址**:
```
    get     /api/v1/user_info/cc_list/
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
    "data": [
        {
            "id": 3,
            "username": "jiangge",
            "role_id": 1,
            "role_name": "admin",
            "name": "bobo",
            "email": "8888888",
            "phone": "132465456",
            "sex": true,
            "department_id": 4,
            "department_name": "销售部",
            "active": true,
            "qr_code": "",
            "create_time": "2018-08-13T01:39:37.833670",
            "update_time": "2018-08-13T01:39:37.833763",
            "wechat": "15314611",
            "leader_id": -1,
            "leader_name": "",
            "is_leader": false
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```