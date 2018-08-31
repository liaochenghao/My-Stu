# coding: utf-8
from rest_framework.routers import SimpleRouter

from .views import OrderViewSet, OrderPaymentViewSet, ShoppingChartViewSet, OrderAdditionalPaymentViewSet, \
    OrderRecordViewSet

router = SimpleRouter()
router.register('order_payment', OrderPaymentViewSet)
router.register('order_record', OrderRecordViewSet)
router.register('order_additional_payment', OrderAdditionalPaymentViewSet)
router.register('shopping_chart', ShoppingChartViewSet)
router.register('order', OrderViewSet)
urlpatterns = router.urls