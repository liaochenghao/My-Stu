### 新增角色

**请求地址**:
```
    POST     /api/v1/role/
```

**请求参数**:
```
{
    "name": str（角色名称） 非空
    "description": str（角色描述信息）, 允许空
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 2,
        "name": "1000",
        "description": "",
        "create_at": "2018-08-07T09:39:19.152668Z",
        "update_at": "2018-08-07T09:39:19.153676Z",
        "enabled": true
    },
    "field_name": ""
}
```

**失败返回**：
```

```