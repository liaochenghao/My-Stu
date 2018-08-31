# coding: utf-8
from rest_framework import routers
from channel.views import ChannelView

router = routers.SimpleRouter()
router.register(r'channel', ChannelView)
urlpatterns = router.urls
