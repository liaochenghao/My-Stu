### 修改角色信息

**请求地址**:
```
    PUT     /api/v1/role/{id}/
```

**请求参数**:
```
{
    "name": str（角色名称） 非空
    "description": str（角色描述信息）, 允许空
    "enabled": boolean  允许空
}
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 1,
        "name": "1000",
        "description": "fwefewfweffwefew",
        "create_at": "2018-08-03T09:10:57.891849Z",
        "update_at": "2018-08-07T09:44:11.259200Z",
        "enabled": true
    },
    "field_name": ""
}
```

**失败返回**：
```

```