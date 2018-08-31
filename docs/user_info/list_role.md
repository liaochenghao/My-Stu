### 查询角色列表

**请求地址**:
```
    GET     /api/v1/role/
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
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "校园大使",
                "description": "fwefewfweffwefew",
                "create_at": "2018-08-03T09:10:57.891849Z",
                "update_at": "2018-08-03T09:12:34.788357Z",
                "enabled": true
            },
            {
                "id": 2,
                "name": "1000",
                "description": "",
                "create_at": "2018-08-07T09:39:19.152668Z",
                "update_at": "2018-08-07T09:39:19.153676Z",
                "enabled": true
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```