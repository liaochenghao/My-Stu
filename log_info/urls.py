# coding: utf-8
from rest_framework import routers

from log_info.views import OperationLogView

router = routers.SimpleRouter()
router.register('log', OperationLogView)
urlpatterns = router.urls
