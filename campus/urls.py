# coding: utf-8
from rest_framework import routers

from campus.views import CampusView

router = routers.SimpleRouter()
router.register('campus', CampusView)
urlpatterns = router.urls
