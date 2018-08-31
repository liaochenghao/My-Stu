from rest_framework import mixins, viewsets
from payment.models import PaymentAccountInfo
from payment.serializers import PaymentAccountInfoSerializer


class PaymentAccountInfoView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    支付方式视图
    """
    queryset = PaymentAccountInfo.objects.all().filter(is_active=True)
    serializer_class = PaymentAccountInfoSerializer
