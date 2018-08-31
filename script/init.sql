insert into department (name, description) values ('市场部', '市场部');
insert into department (name, description) values ('产品部', '产品部');
insert into department (name, description) values ('财务部', '财务部');
insert into department (name, description) values ('销售部', '销售部');


insert into menu (id, name, url, parent_id, extra) values (1, '系统菜单', '/var/www/user.html', -1, '');
insert into menu (id, name, url, parent_id, extra) values (2, '超级管理中心', '/var/www/user.html', 1, '');
insert into menu (id, name, url, parent_id, extra) values (3, '产品管理中心', '/var/www/project.html', 1, '');
insert into menu (id, name, url, parent_id, extra) values (4, '报名咨询中心', '/var/www/student.html', 1, '');
insert into menu (id, name, url, parent_id, extra) values (5, '学服中心', '/var/www/order.html', 1, '');
insert into menu (id, name, url, parent_id, extra) values (6, '财务中心', '/var/www/market.html', 1, '');
insert into menu (id, name, url, parent_id, extra) values (7, '优惠中心', '/var/www/finance.html', 1, '');
insert into menu (id, name, url, parent_id, extra) values (8, '角色管理', '/var/www/role.html', 2, '');
insert into menu (id, name, url, parent_id, extra) values (9, '用户管理', '/var/www/user.html', 2, '');
insert into menu (id, name, url, parent_id, extra) values (10, '部门管理', '/var/www/department.html', 2, '');
insert into menu (id, name, url, parent_id, extra) values (11, '超级日志', '/var/www/department.html', 2, '');
insert into menu (id, name, url, parent_id, extra) values (12, '开课统计', '/var/www/campus.html', 3, '产品');
insert into menu (id, name, url, parent_id, extra) values (13, '课程管理', '/var/www/course.html', 3, '');
insert into menu (id, name, url, parent_id, extra) values (14, '项目管理', '/var/www/project.html', 3, '');
insert into menu (id, name, url, parent_id, extra) values (15, '中心首页', '/var/www/campus.html', 4, '咨询');
insert into menu (id, name, url, parent_id, extra) values (16, '学生列表', '/var/www/campus.html', 4, '咨询');
insert into menu (id, name, url, parent_id, extra) values (17, '开课统计', '/var/www/campus.html', 4, '咨询');
insert into menu (id, name, url, parent_id, extra) values (18, '中心首页', '/var/www/campus.html', 5, '学服');
insert into menu (id, name, url, parent_id, extra) values (19, '学生列表', '/var/www/campus.html', 5, '学服');
insert into menu (id, name, url, parent_id, extra) values (20, '财务管理', '/var/www/campus.html', 6, '');
insert into menu (id, name, url, parent_id, extra) values (21, '缴费凭据管理', '/var/www/campus.html', 6, '');
insert into menu (id, name, url, parent_id, extra) values (22, '支付账号管理', '/var/www/campus.html', 6, '');
insert into menu (id, name, url, parent_id, extra) values (23, '固定优惠管理', '/var/www/campus.html', 6, '');
insert into menu (id, name, url, parent_id, extra) values (24, '固定优惠规则', '/var/www/campus.html', 6, '');
insert into menu (id, name, url, parent_id, extra) values (25, '学生列表', '/var/www/campus.html', 6, '财务');

