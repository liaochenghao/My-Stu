# 后台接口文档

### 数据返回格式

**统一为 `json` 格式**:
```
    {
        "code": 0,
        "msg": "success",
        "data": {
            ... // 数据内容
        }
        field_name: ""
    }
```
- code `int` 0为成功，非0为失败 (code=401表示未登录)
- msg `string` 成功或失败的消息
- data `dict` 返回的数据内容
- field_name: `str`  code为非0状态时，报错字段


### API接口文档

**系统用户模块**
- [查询部门列表](docs/user_info/list_department.md)
- [新增部门](docs/user_info/create_department.md)
- [查看部门详情](docs/user_info/detail_department.md)
- [修改部门信息](docs/user_info/update_department.md)
- [查询角色列表](docs/user_info/list_role.md)
- [获取角色详情](docs/user_info/detail_role.md)
- [创建角色](docs/user_info/create_role.md)
- [修改角色信息](docs/user_info/update_role.md)
- [根据角色获取访问权限菜单树](docs/user_info/get_privilege_by_role.md)
- [设置用户访问权限菜单](docs/user_info/set_privilege.md)
- [创建用户](docs/user_info/create_user.md)
- [查看用户列表](docs/user_info/list_user.md)
- [查看用户详情](docs/user_info/detail_user.md)
- [修改用户信息](docs/user_info/update_user.md)
- [检查用户的菜单访问权限](docs/user_info/check_visit_url.md)
- [后台用户登录接口](docs/user_info/login.md)
- [获取销售部门人员列表](docs/user_info/cc_list.md)

**学生信息**

- [CODE验证](docs/student/code_auth.md)
- [获取学生信息列表](docs/student/get_student_list.md)
- [获取学生信息](docs/student/get_student_info.md)
- [更新学生信息](docs/student/update_student_info.md)
- [创建用户成绩邮寄信息](docs/student/create_score_detail.md)
- [获取用户成绩邮寄信息](docs/student/get_score_detail.md)
- [修改用户成绩邮寄信息](docs/student/update_score_detail.md)
- [创建学生协议](docs/student/create_agreement.md)
- [获取渠道记录](docs/record/record.md)

**学生审课模块**:
- [获取学生审课](docs/student_course/review/review.md)
- [根据学生id获取审课方案](docs/student_course/review/get_review_by_student_id.md)
- [添加学生审课](docs/student_course/review/add_review.md)
- [修改学生审课](docs/student_course/review/update_review.md)

**学生审课课程模块**:
- [获取审课方案课程](docs/student_course/review_course/review_course.md)
- [上传审课凭据](docs/student_course/review_course/upload_certificate.md)
- [查看审课凭据](docs/student_course/review_course/get_certificate.md)
- [根据学生id获取学生审课方案表](docs/student_course/review_course/get_review_course_by_student_id.md)
- [确认审课成功](docs/student_course/review_course/confirm_review_course.md)
- [确认审课失败](docs/student_course/review_course/deny_review_course.md)
- [添加审课方案课程](docs/student_course/review_course/add_review_course.md)
- [修改审课方案课程](docs/student_course/review_course/update_review_course.md)

**学生确认课程模块**:
- [获取确认课程](docs/student_course/confirm_course/confirm_course.md)
- [添加确认课程](docs/student_course/confirm_course/add_confirm_course.md)
- [修改确认课程](docs/student_course/confirm_course/update_confirm_course.md)
- [根据学生id获取确认课程](docs/student_course/confirm_course/get_confirm_course.md)
- [根据课程id搜索项目](docs/student_course/confirm_course/get_project.md)
- [根据学生id获取审课-项目信息](docs/student_course/confirm_course/review_project.md)
- [根据学生id获取学服老师及确认课程时间](docs/student_course/confirm_course/get_server_time.md)
- [删除学生课程](docs/student_course/confirm_course/del_course.md)

**学生成绩模块**:
- [根据学生id查询成绩](docs/student_course/confirm_course/query_performance.md)
- [根据学生id查询快递](docs/student_course/confirm_course/get_recipient.md)
- [确认成绩](docs/student_course/confirm_course/confirm_performance.md)
- [录入学生成绩等级或快递信息](docs/student_course/confirm_course/score_recipient.md)

**学生转学分模块**:
- [根据学生id获取学分转换信息](docs/student_course/confirm_course/get_student_convert.md)
- [用户上传转学分图片](docs/student_course/confirm_course/upload_convert.md)
- [查看用户转学分图片](docs/student_course/confirm_course/get_convert.md)
- [确认转学分成功](docs/student_course/confirm_course/confirm_convert.md)
- [确认转学分失败](docs/student_course/confirm_course/deny_convert.md)

**学生调课记录模块**:
- [获取学生调课记录](docs/student_course/change_course_record/change_course_record.md)
- [根据学生id获取课程调整记录](docs/student_course/change_course_record/get_change_record.md)
- [添加学生调课记录](docs/student_course/change_course_record/add_change_course_record.md)
- [修改学生调课记录](docs/student_course/change_course_record/update_change_course_record.md)

**开课列表模块**
- [获取开课列表](docs/open_course/get_project_course.md)
- [根据校区和项目搜索开课列表](docs/open_course/search_course_by_campus_project.md)
- [根据课程id搜索开课列表](docs/open_course/search_course_by_course_id.md)
- [查看关联审课课程](docs/open_course/relate_review_course.md)
- [获取开课列表选课学生名单](docs/open_course/get_select_student.md)

**校区管理模块**:
- [获取校区](docs/campus/campus.md)
- [获取所有校区id和name](docs/campus/all.md)
- [添加校区](docs/campus/add_campus.md)
- [修改校区](docs/campus/update_campus.md)

**课程管理模块**
- [获取课程](docs/course/course.md)
- [获取所有课程id和name](docs/course/all.md)
- [添加课程](docs/course/add_course.md)
- [修改课程](docs/course/update_course.md)
- [根据项目id搜索课程](docs/course/search_course_by_project_id.md)
- [查看关联审课课程](docs/course/get_relate_review_course.md)
- [根据课程id获取关联项目](docs/course/get_relate_project_by_course_id.md)
- [取消关联项目](docs/course/delete_relate_project.md)

**项目管理模块**
- [获取项目](docs/project/project.md)
- [获取所有项目id和name](docs/project/all.md)
- [添加项目](docs/project/add_project.md)
- [修改项目](docs/project/update_project.md)
- [获取校区关联项目](docs/project/get_project_by_campus.md)
- [获取课程关联项目](docs/project_course/project_course.md)
- [修改课程关联项目](docs/project_course/update_project_course.md)
- [根据项目id获取关联课程](docs/project_course/get_relate_course_by_project_id.md)
- [取消关联课程](docs/project_course/delete_relate_course.md)
- [添加课程关联项目](docs/project_course/add_project_course.md)

**公共信息模块**

- [成绩查询时间信息](docs/common/context.md)


**支付模块**:
- [获取学校](docs/campus/campus.md)
- [获取校区关联项目](docs/project/get_project_by_campus.md)

**购物车模块**:
- [创建购物车](docs/shopping_chart/create_shopping_chart.md )
- [获取购物车列表](docs/shopping_chart/shopping_chart_list.md)
- [删除购物车](docs/shopping_chart/delete_shopping_chart.md)
- [修改购物车](docs/shopping_chart/update_shopping_chart.md)
- [批量修改购物车](docs/shopping_chart/update_shopping_chart_list.md)
- [批量删除购物车](docs/shopping_chart/delete_shopping_chart_list.md)
- [获取购物车项目](docs/shopping_chart/shopping_chart_project_list.md)

**订单模块**:
- [创建订单](docs/order/create_order.md)
- [取消订单](docs/order/cancel_order.md)
- [获取订单列表](docs/order/order_list.md)
- [获取学生订单列表](docs/order/user_order_list.md)
- [后台获取学生订单列表](docs/order/admin_user_order_list.md)
- [获取订单详细信息](docs/order/order_detail.md)
- [获取最新订单详细信息](docs/order/last_order_detail.md)
- [获取最终订单信息](docs/order/final_order_detail.md)

- [创建订单支付信息](docs/order/create_order_payment.md)
- [获取订单支付信息](docs/order/get_order_payment.md)
- [创建订单补缴/退费信息](docs/order/create_order_additional_payment.md)
- [修改订单补缴/退费信息](docs/order/update_order_additional_payment.md)
- [获取订单补缴/退费信息](docs/order/get_order_additional_payment.md)
- [获取订单补缴/退费信息列表](docs/order/get_order_additional_payment_list.md)

**推荐模块**:
- [查看当前用户推荐(手机端)](docs/record/current_invitation.md)
- [查看当前用户推荐(后台)](docs/record/current_invitation_back.md)

**消息模块**:
- [查看当前学生消息列表](docs/message/list_message.md)
- [添加学生消息](docs/message/create_message.md)
- [修改学生消息](docs/message/update_message.md)