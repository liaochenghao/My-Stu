# coding: utf-8
from rest_framework.routers import SimpleRouter
from .views import StudentInfoViewSet, StudentScoreDetailViewSet, StudentAgreementView

router = SimpleRouter()
router.register('student/info', StudentInfoViewSet)  # 用户信息
router.register('student/score_detail', StudentScoreDetailViewSet)  # 成绩单寄送地址视图
router.register('student/agreement', StudentAgreementView)  # 学生协议视图

urlpatterns = router.urls
