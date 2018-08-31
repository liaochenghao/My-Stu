# Create your views here.
from rest_framework import mixins, viewsets
from coupon.models import Coupon
from coupon.serializers import CouponSerializer


class CouponView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                 mixins.ListModelMixin):
    queryset = Coupon.objects.all().filter()
    serializer_class = CouponSerializer

