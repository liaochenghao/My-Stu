### 获取用户成绩寄送地址详情

**请求地址**:
```
    GET     /api/v1/student/score_detail/
```

**请求参数**:
```
    user    选填
    
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "user": 2,
                "country": "美国",
                "region": "纽约",
                "city": "纽约",
                "address1": "地址一",
                "address2": "地址二",
                "post_code": "888",
                "recipient": "收件人",
                "recipient_phone": "18888888888",
                "recipient_number": "888888888",
                "sending_date": "2018-08-10",
                "post_status": null
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```