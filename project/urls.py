# coding: utf-8
from rest_framework import routers

from project.views import ProjectView, ProjectCourseView

router = routers.SimpleRouter()
router.register('project', ProjectView)
router.register('project_course', ProjectCourseView)
urlpatterns = router.urls
