### 查看当前用户推荐信息

**请求地址**:
```
    GET     /api/v1/record/recommend/success_by_student
```

**请求参数**:
```
{
    "student_id": str ,
    "tag": true/false   (true表示取最新5条记录)
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "id": 4,
            "name": "jkl",
            "student_status": "缴费确认成功",
            "cschool": "qwe",
            "last_login": "2018-08-24T10:04:40",
            "cc": "15",
            "server": null,
            "invite_time": "2018-08-22T14:23:26"
        },
        {
            "id": 3,
            "name": "dsf",
            "student_status": "缴费确认成功",
            "cschool": "sdf",
            "last_login": "2018-08-24T10:04:36",
            "cc": "54",
            "server": "lebron",
            "invite_time": "2018-08-22T14:22:26"
        },
        {
            "id": 2,
            "name": "卡哇伊",
            "student_status": "缴费确认成功",
            "cschool": "佐治亚大学",
            "last_login": "2018-08-24T10:04:33",
            "cc": "15",
            "server": "kanyewest",
            "invite_time": "2018-08-22T14:21:26"
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```