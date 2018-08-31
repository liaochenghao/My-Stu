### 获取学生信息列表

**请求地址**:
```
    GET     /api/v1/student/info/
```


**请求参数**:
```
    过滤字段:
        all_payment_student,      True为获取所有已缴费学生

        name            姓名
        email           邮件
        wechat          微信 
        cc              cc
        student_status  状态
        create_year     年
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 4,
        "name": "jkl",
        "birth_date": null,
        "cschool": "qwe",
        "major": null,
        "email": "asdd123@qq.com",
        "wechat": null,
        "student_status": "PERSONAL_FILE",
        "cc": "15",
        "server": null,
        "first_name": null,
        "phone": null,
        "gender": {
            "key": "MALE",
            "verbose": "男"
        },
        "school_email": null,
        "id_number": null,
        "enrollment_year": null,    入学年份
        "student_number": null,     学生证号
        "gpa": null,
        "cc_sign": false,           CC标记
        "server_sign": false,       学服标记
        "card_img1": null,
        "card_img2": null,
        "last_name": null,
        "qr_code": null,
        "transcript_img": null,     成绩单
        "intention": 0,             意向
        "contact": null,            紧急联系人
        "contact_relation": null,   紧急联系人关系
        "contact_wechat": null,
        "contact_email": null,
        "modified_time": "2018-08-23T19:16:07"  跟进时间 
    },
    "field_name": ""
}

**失败返回**：
```

```