### 修改用户成绩寄送地址

**请求地址**:
```
    PUT/PATCH     /api/v1/student/score_detail/[score_detail_id]/
```

**请求参数**:
```
{
    "post_code": ""             str     收件州/省的邮编  
    "university": ""            str     大学名称   
    "country": ""                str     国家
    "city": ""                  str     城市
    "address1": ""              str     地址一
    "address2"：""              str     地址一
    "recipient"：""              str     收件人姓名
    "sending_date":    ""       str     发件日期 
    "post_status":    ""        str     邮件状态  
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