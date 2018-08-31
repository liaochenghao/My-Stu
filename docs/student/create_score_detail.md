###     用户成绩邮寄信息创建

**请求地址**:
```
   POST     /api/v1/student/score_detail/
```

**请求参数**:
```
{
    "post_code": ""             str     收件州/省的邮编  
    "region": ""               str     地区   
    "country": ""                str     国家
    "city": ""                  str     城市
    "address1": ""              str     地址一
    "address2"：""              str     地址一
    "recipient"：""              str     收件人姓名
    "recipient_phone":    ""     str     联系电话 

}
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
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```