# coding: utf-8
from rest_framework import routers

from coupon.views import CouponView

router = routers.SimpleRouter()
router.register(r'coupon', CouponView)
urlpatterns = router.urls
