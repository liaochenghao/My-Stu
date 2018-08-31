### 检查用户的菜单访问权限

**请求地址**:
```
    POST     /api/v1/user_info/check_url/
```

**请求参数**:
```
{
    visit_url: str（菜单访问你地址） 必填
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": "true/false",
    "field_name": ""
}
```

**失败返回**：
```

```