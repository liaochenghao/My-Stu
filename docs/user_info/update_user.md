### 查询用户列表

**请求地址**:
```
    PUT     /api/v1/user_info/basic_info_update/
```

**请求参数**:
```
{
    "id": str (用户编号),
    "name": str (用户姓名),
    "sex": Boolean (用户性别),
    "email": str (邮箱),
    "phone": str (手机号码),
    "leader_id": int (直接领导人编号),
    "leader_name": str (直接领导姓名),
    "extra": str (备注),
    "department_id": int (部门编号),
    "department_name": int (部门名称),
    "role_id": int (角色编号),
    "role_name": int (角色名称),
    "qr_code": base64图片(二维码),
    "active": Boolean (是否禁用),
    "wechat": str (微信),
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": null,
    "field_name": ""
}
```

**失败返回**：
```

```