### 创建订单补缴/退费信息

**请求地址**:
```
    POST   /api/v1/order_additional_payment/
```

**请求参数**:
```
{   
    "type":             str     类型          必填
    "replenish_type":   str     补缴类型      选填
    "refunded_type":    str     退费类型      选填
    "order":            int     订单id        必填
    "user":             int     学生          必填
    "amount":           str     金额          必填
    "currency":         str     币种          必填
    "project":          str     项目          选填
    "course_num":       str     课程数量      选填
    "admin_remark":     str     备注          选填
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