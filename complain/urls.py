# coding: utf-8
from rest_framework import routers

from complain.views import ComplainView

router = routers.SimpleRouter()
router.register('complain', ComplainView)
urlpatterns = router.urls
