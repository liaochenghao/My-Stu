### 获取校区关联项目

**请求地址**:
```
    GET     /api/v1/project/get_project_by_campus/{campus_id}
```

**请求参数**:
```
{
    校区名称：campus_id int
 }  
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": [
        "北京一期项目",
        "武汉二期项目"
    ],
    "field_name": ""
}
```

**失败返回**：
```

```