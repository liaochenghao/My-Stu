# coding: utf-8
from rest_framework import routers
from record.views import ChannelRecordView, RecommendRecordView

router = routers.SimpleRouter()
router.register('record/channel', ChannelRecordView)
router.register('record/recommend', RecommendRecordView)
urlpatterns = router.urls
