### 根据学生id获取学生审课方案表

**请求地址**:
```
    GET     /api/v1/review_course/get_review_course/{student_id}
```

**请求参数**:
```
{
    student_id  学生id int
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "id": 3,
            "create_time": "2018-08-08T10:29:20",
            "modified_time": "2018-08-25T18:02:50",
            "course_detail": [
                {
                    "id": 3,
                    "review": 3,
                    "school": "上海财经大学",
                    "course_code": "42",
                    "course_name": "计算机科学",
                    "course__name": "金融学123415646",
                    "status": "SUCCESS",
                    "review_certificate": "images/certificate/69142fa5-334c-4f63-b340-0dcaa8683af4.png",
                    "real_name": null
                }
            ]
        },
        {
            "id": 6,
            "create_time": "2018-08-08T10:28:34",
            "modified_time": "2018-08-25T18:02:58",
            "course_detail": [
                {
                    "id": 5,
                    "review": 6,
                    "school": "重庆大学",
                    "course_code": "11",
                    "course_name": "微积分",
                    "course__name": "计算机与科学",
                    "status": "WAIT_CERTIFICATE",
                    "review_certificate": "images/certificate/410e4984-51f1-4f4d-b1af-d2dac8e61ff6.png",
                    "real_name": null
                }
            ]
        },
        {
            "id": 7,
            "create_time": "2018-08-27T16:01:04.159000",
            "modified_time": "2018-08-27T16:01:04.159000",
            "course_detail": []
        },
        {
            "id": 9,
            "create_time": "2018-08-28T14:16:15.658000",
            "modified_time": "2018-08-28T14:16:15.659000",
            "course_detail": []
        },
        {
            "id": 10,
            "create_time": "2018-08-28T14:21:08.547000",
            "modified_time": "2018-08-28T14:21:08.547000",
            "course_detail": []
        },
        {
            "id": 11,
            "create_time": "2018-08-28T14:22:51.238000",
            "modified_time": "2018-08-28T14:22:51.238000",
            "course_detail": [
                {
                    "id": 11,
                    "review": 11,
                    "school": "深圳大学",
                    "course_code": "11",
                    "course_name": "线性代数",
                    "course__name": "金融学123415646",
                    "status": "WAIT_CERTIFICATE",
                    "review_certificate": null,
                    "real_name": null
                },
                {
                    "id": 12,
                    "review": 11,
                    "school": "深圳大学",
                    "course_code": "22",
                    "course_name": "线性代数",
                    "course__name": "数学7894",
                    "status": "WAIT_CERTIFICATE",
                    "review_certificate": null,
                    "real_name": null
                }
            ]
        },
        {
            "id": 12,
            "create_time": "2018-08-28T15:36:46.305000",
            "modified_time": "2018-08-28T15:36:46.305000",
            "course_detail": [
                {
                    "id": 13,
                    "review": 12,
                    "school": "深圳大学",
                    "course_code": "22",
                    "course_name": "线性代数",(课程别名)
                    "course__name": "数学7894",(课程原名)
                    "status": "WAIT_CERTIFICATE",
                    "review_certificate": null,
                    "real_name": "数学7894"
                },
                {
                    "id": 14,
                    "review": 12,
                    "school": "杭州大学",
                    "course_code": "111",
                    "course_name": "市场营销",
                    "course__name": "市场营销",
                    "status": "WAIT_CERTIFICATE",
                    "review_certificate": null,
                    "real_name": "市场营销"
                }
            ]
        }
    ],
```

**失败返回**：
```

```