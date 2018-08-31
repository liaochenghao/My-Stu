from django.conf.urls import url
from rest_framework import routers
from user_info.views import DepartmentView, PrivilegeView, MenuView, UserInfoView, TestView, RoleView

router = routers.SimpleRouter()
router.register(r'department', DepartmentView)
router.register(r'role', RoleView)
router.register(r'privilege', PrivilegeView)
router.register(r'menu', MenuView)
router.register(r'user_info', UserInfoView)
urlpatterns = router.urls

urlpatterns += [
    url(r'^test', TestView.as_view())
]
