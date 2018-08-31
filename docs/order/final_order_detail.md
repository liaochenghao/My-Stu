### 获取最终订单详情


**请求地址**:
```
    GET /api/v1/order_record/get_final_order/
```

**请求参数**:
```
    student_id
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
                "order": 11,
                "project1": 1,
                "course_num1": 1,
                "project2": null,
                "course_num2": null,
                "project3": null,
                "course_num3": null,
                "project4": null,
                "course_num4": null,
                "all_amount": 111.0
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```