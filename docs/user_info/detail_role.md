### 查询角色详情

**请求地址**:
```
    GET     /api/v1/role/{id}
```

**请求参数**:
```
{
    id: str (角色ID)
}
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 1,
        "name": "校园大使",
        "description": "fwefewfweffwefew",
        "create_at": "2018-08-03T09:10:57.891849Z",
        "update_at": "2018-08-03T09:12:34.788357Z",
        "enabled": true
    },
    "field_name": ""
}
```

**失败返回**：
```

```