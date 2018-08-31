###     创建学习协议

**请求地址**:
```
   POST     /api/v1/student/agreement/
```

**请求参数**:
```
{
    "image": ""       file    学生签名图片  
    "user_id": ""     str     学生编号  
  }
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 9,
        "user_id": 1,
        "agreement": "agreement/1_agreement.png",
        "create_time": "2018-08-09T08:43:25.452188Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```