### 部门列表

**请求地址**:
```
    GET     /api/v1/department/
```

**请求参数**:
```
{
    无
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "count": 4,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "学服部",
                "description": "",
                "leader_id": "",
                "leader_name": "",
                "create_at": "2018-08-03T08:27:13.024426Z",
                "update_at": "2018-08-03T08:27:13.025390Z",
                "enabled": true
            },
            {
                "id": 2,
                "name": "技术部",
                "description": "",
                "leader_id": "",
                "leader_name": "",
                "create_at": "2018-08-03T09:01:55.560993Z",
                "update_at": "2018-08-03T09:01:55.562988Z",
                "enabled": true
            },
            {
                "id": 3,
                "name": "销售11部",
                "description": "",
                "leader_id": "123",
                "leader_name": "bobo",
                "create_at": "2018-08-03T09:02:19.020844Z",
                "update_at": "2018-08-03T09:06:32.965907Z",
                "enabled": false
            },
            {
                "id": 4,
                "name": "1000",
                "description": "",
                "leader_id": "",
                "leader_name": "",
                "create_at": "2018-08-07T09:22:02.013032Z",
                "update_at": "2018-08-07T09:22:02.015027Z",
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