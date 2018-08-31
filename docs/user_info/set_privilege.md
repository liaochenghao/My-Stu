### 设置用户菜单访问权限

**请求地址**:
```
     POST     /api/v1/privilege/set_current_privilege/
```

**请求参数**:
```
{
    role_id: str（角色编号） 必填
    menu_id_list: str（菜单列表[1,2,3,11,12,22,23,31]）  注意：子菜单选中的时候，父菜单一定要选中
    
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": "",
    "field_name": ""
}
```

**失败返回**：
```

```