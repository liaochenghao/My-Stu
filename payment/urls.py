# coding: utf-8
from rest_framework import routers

from payment.views import PaymentAccountInfoView

router = routers.SimpleRouter()
router.register('payment', PaymentAccountInfoView)
urlpatterns = router.urls
