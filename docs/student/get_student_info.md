### 获取用户信息

**请求地址**:
```
    GET     /api/v1/student/info/[user_id]/
```


**请求参数**:
```
    无
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 2,
        "name": "霸王别姬",
        "birth_date": "2018-08-09",
        "cschool": "武汉大学",
        "major": "计算机",
        "email": "abc@163.com",
        "wechat": "WeChat",
        "student_status": {
            "key": "NEW",
            "verbose": "新建用户"
        },
        "cc": null,
        "server": null,
        "english_name": "English",
        "phone": "18888888888",
        "gender": {
            "key": "MALE",
            "verbose": "男"
        },
        "school_email": "school@school.com",
        "id_number": "123456789",
        "enrollment_year": "2018",
        "student_number": "888888",
        "gpa": 3.0,
        "cc_sign": false,
        "server_sign": false,
        "card_img1": "http://127.0.0.1:8004/media/IDcard1/timg.jpg",
        "card_img2": "http://127.0.0.1:8004/media/IDcard2/timg.jpg",
        "transcript_img": "http://127.0.0.1:8004/media/transcript/timg.jpg",
        "intention": 3,
        "contact": "项羽",
        "contact_relation": "自己",
        "contact_wechat": "WeChat",
        "contact_email": "123@qq.com"
    },
    "field_name": ""
}

**失败返回**：
```

```