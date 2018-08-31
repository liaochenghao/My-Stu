### 获取订单补缴/退费信息

**请求地址**:
```
    GET   /api/v1/order_additional_payment/get_info/
```

**请求参数**:
```
    order_id     订单ID
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 7,
        "order_id": 11,
        "amount": 234,
        "img": "https://cp1.lxhelper.com/media/order/e8db5276-319.jpg",
        "account_name": "wer",
        "phone": "123123",
        "relation": "sf",
        "remark": "fsf",
        "create_time": "2018-08-15T03:27:28.962880Z"
    },
    "field_name": ""
}
```

**失败返回**：
```

```