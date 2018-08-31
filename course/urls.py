# coding: utf-8
from rest_framework import routers

from course.views import CourseView

router = routers.SimpleRouter()
router.register('course', CourseView)
urlpatterns = router.urls
