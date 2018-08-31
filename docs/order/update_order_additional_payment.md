### 修改订单补缴/退费信息

**请求地址**:
```
    PUT   /api/v1/order_additional_payment/[id]/
```

**请求参数**:
```
{
    "img":          Base64   确认图片,
    "student_remark":       str     备注       选填
}
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 9,
        "img": "http://42.51.8.152:8002/media/order/order_payment/70277236478236737_kMl8gmx.jpg",
        "order": 1,
        "remark": "222111111111111111111"
    },
    "field_name": ""
}
```

**失败返回**：
```

```