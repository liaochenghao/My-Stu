# coding: utf-8
from rest_framework import routers

from message.views import StudentMessageView

router = routers.SimpleRouter()
router.register('message/student', StudentMessageView)
urlpatterns = router.urls
