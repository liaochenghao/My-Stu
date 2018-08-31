### 删除学生课程

**请求地址**:
```
    POST     /api/v1/change_course_record/del_course/
```

**请求参数**:
```
{
         "course_code": str 课程代码 ,
         "student_id": 学生id int ,
         "extra":   备注 str
}
```


**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": "操作成功!",
    "field_name": ""
}
```
**失败返回**：
```

```