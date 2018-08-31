### 上传转学分图片

**请求地址**:
```
    POST    /api/v1/confirm_course/upload_convert/
```

**请求参数**:
```
{
         "course_code": str 课程代码 ,        
         "course_name": str 课程名称 ,
         "image": 64位编码 转学分图片 ,
         "remark":   str 备注 可为空,
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": "转学分图片上传成功！",
    "field_name": ""
}
```

**失败返回**：
```

```