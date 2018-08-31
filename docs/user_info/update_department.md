### 修改部门信息

**请求地址**:
```
    PUT     /api/v1/department/{id}/
```

**请求参数**:
```
{
    name : str （部门名称）,
    description : str （部门描述）,
    leader_id : str （部门领导编号）,
    leader_name : str （部门领导名称）,
    enabled : boolean （是否启用）,
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
        "description": "",
        "leader_id": "",
        "leader_name": "",
        "create_at": "2018-08-03T08:27:13.024426Z",
        "update_at": "2018-08-07T09:30:09.539319Z",
        "enabled": true
    },
    "field_name": ""
}
```

**失败返回**：
```

```