### 上传审课凭据

**请求地址**:
```
    POST    /api/v1/review_course/upload_certificate/
```

**请求参数**:
```
{
         "course_code": str 课程代码 ,        
         "course_name": str 课程名称 ,
         "certificate": file 审课凭据 ,
         "remark":   str 备注 允许为空，
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": "审课凭据上传成功！",
    "field_name": ""
}
```

**失败返回**：
```

```