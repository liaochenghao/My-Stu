### 获取所有项目id和name

**请求地址**:
```
    GET     /api/v1/project/all/
```

**请求参数**:
```
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "id": 1,
            "name": "北京一期项目"
        },
        {
            "id": 2,
            "name": "武汉一期项目"
        },
        {
            "id": 3,
            "name": "重庆一期项目"
        },
        {
            "id": 4,
            "name": "上海一期项目"
        },
        {
            "id": 5,
            "name": "一期"
        },
        {
            "id": 7,
            "name": "4"
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```