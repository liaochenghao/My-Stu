### 取消关联项目

**请求地址**:
```
    PATCH     /api/v1/project_course/{id}/
```

**请求参数**:
```
{
    id 项目课程关联id int
    status 是否删除 bool false
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": null,
    "field_name": ""
}
```

**失败返回**：
```

```