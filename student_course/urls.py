# coding: utf-8
from rest_framework.routers import SimpleRouter

from student_course.views import ReviewView, ReviewCourseView, ConfirmCourseView, ChangeCourseRecordView

router = SimpleRouter()
router.register('review', ReviewView)
router.register('review_course', ReviewCourseView)
router.register('confirm_course', ConfirmCourseView)
router.register('change_course_record', ChangeCourseRecordView)

urlpatterns = router.urls
