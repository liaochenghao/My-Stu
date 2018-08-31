### 获取课程项目关联信息

**请求地址**:
```
    GET     /api/v1/project_course/{id}
```

**请求参数**:
```
{
    id
    不加id参数返回所有课程项目信息
 }  
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 1,
        "modified_time": "2018-08-06T11:11:41Z",
        "create_time": "2018-08-06T11:11:38Z",
        "status": false,
        "course": 1,
        "project": 1,
        "course_name": "k1"
    },
    "field_name": ""
}
```

**失败返回**：
```

```