### 根据角色获取菜单访问权限

**请求地址**:
```
    GET     /api/v1/privilege/get_current_privilege
```

**请求参数**:
```
{
    role_id: str （角色编号） 必填
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "id": 2,
            "name": "超级管理中心",
            "url": "/var/www/user.html",
            "parent_id": 1,
            "extra": "",
            "create_at": null,
            "children": [
                {
                    "id": 8,
                    "name": "角色管理",
                    "url": "/var/www/role.html",
                    "parent_id": 2,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": true
                },
                {
                    "id": 9,
                    "name": "用户管理",
                    "url": "/var/www/user.html",
                    "parent_id": 2,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": true
                },
                {
                    "id": 10,
                    "name": "部门管理",
                    "url": "/var/www/department.html",
                    "parent_id": 2,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": true
                },
                {
                    "id": 11,
                    "name": "超级日志",
                    "url": "/var/www/department.html",
                    "parent_id": 2,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": true
                }
            ],
            "choose": true
        },
        {
            "id": 3,
            "name": "产品管理中心",
            "url": "/var/www/project.html",
            "parent_id": 1,
            "extra": "",
            "create_at": null,
            "children": [
                {
                    "id": 12,
                    "name": "开课统计产品",
                    "url": "/var/www/campus.html",
                    "parent_id": 3,
                    "extra": "产品",
                    "create_at": null,
                    "children": [],
                    "choose": true
                },
                {
                    "id": 13,
                    "name": "课程管理",
                    "url": "/var/www/course.html",
                    "parent_id": 3,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": true
                },
                {
                    "id": 14,
                    "name": "项目管理",
                    "url": "/var/www/project.html",
                    "parent_id": 3,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": true
                }
            ],
            "choose": true
        },
        {
            "id": 4,
            "name": "报名咨询中心",
            "url": "/var/www/student.html",
            "parent_id": 1,
            "extra": "",
            "create_at": null,
            "children": [
                {
                    "id": 15,
                    "name": "中心首页咨询",
                    "url": "/var/www/campus.html",
                    "parent_id": 4,
                    "extra": "咨询",
                    "create_at": null,
                    "children": [],
                    "choose": true
                },
                {
                    "id": 16,
                    "name": "学生列表咨询",
                    "url": "/var/www/campus.html",
                    "parent_id": 4,
                    "extra": "咨询",
                    "create_at": null,
                    "children": [],
                    "choose": true
                },
                {
                    "id": 17,
                    "name": "开课统计咨询",
                    "url": "/var/www/campus.html",
                    "parent_id": 4,
                    "extra": "咨询",
                    "create_at": null,
                    "children": [],
                    "choose": false
                }
            ],
            "choose": true
        },
        {
            "id": 5,
            "name": "学服中心",
            "url": "/var/www/order.html",
            "parent_id": 1,
            "extra": "",
            "create_at": null,
            "children": [
                {
                    "id": 18,
                    "name": "中心首页学服",
                    "url": "/var/www/campus.html",
                    "parent_id": 5,
                    "extra": "学服",
                    "create_at": null,
                    "children": [],
                    "choose": false
                },
                {
                    "id": 19,
                    "name": "学生列表学服",
                    "url": "/var/www/campus.html",
                    "parent_id": 5,
                    "extra": "学服",
                    "create_at": null,
                    "children": [],
                    "choose": false
                }
            ],
            "choose": true
        },
        {
            "id": 6,
            "name": "财务中心",
            "url": "/var/www/market.html",
            "parent_id": 1,
            "extra": "",
            "create_at": null,
            "children": [
                {
                    "id": 20,
                    "name": "财务管理",
                    "url": "/var/www/campus.html",
                    "parent_id": 6,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": false
                },
                {
                    "id": 21,
                    "name": "缴费凭据管理",
                    "url": "/var/www/campus.html",
                    "parent_id": 6,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": false
                },
                {
                    "id": 22,
                    "name": "支付账号管理",
                    "url": "/var/www/campus.html",
                    "parent_id": 6,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": false
                },
                {
                    "id": 23,
                    "name": "固定优惠管理",
                    "url": "/var/www/campus.html",
                    "parent_id": 6,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": false
                },
                {
                    "id": 24,
                    "name": "固定优惠规则",
                    "url": "/var/www/campus.html",
                    "parent_id": 6,
                    "extra": "",
                    "create_at": null,
                    "children": [],
                    "choose": false
                },
                {
                    "id": 25,
                    "name": "学生列表财务",
                    "url": "/var/www/campus.html",
                    "parent_id": 6,
                    "extra": "财务",
                    "create_at": null,
                    "children": [],
                    "choose": false
                }
            ],
            "choose": true
        },
        {
            "id": 7,
            "name": "优惠中心",
            "url": "/var/www/finance.html",
            "parent_id": 1,
            "extra": "",
            "create_at": null,
            "children": [],
            "choose": true
        }
    ],
    "field_name": ""
}
```

**失败返回**：
```

```