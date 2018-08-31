### 新增部门

**请求地址**:
```
    POST     /api/v1/department/
```

**请求参数**:
```
{
    "name": str（部门名称） 非空
    "description": str（部门描述信息）, 允许空
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 4,
        "name": "技术部",
        "description": "技术部",
        "leader_id": "",
        "leader_name": "",
        "create_at": "2018-08-07T09:22:02.013032Z",
        "update_at": "2018-08-07T09:22:02.015027Z",
        "enabled": true
    },
    "field_name": ""
}
```

**失败返回**：
```

```