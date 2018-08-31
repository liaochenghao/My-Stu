# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from common.models import Common
from common.serializers import CommonSerializer


class CommonView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    公共信息视图
    """
    queryset = Common.objects.all()
    serializer_class = CommonSerializer

    @list_route(['GET'])
    def context(self, request):
        return Response(self.queryset.values('context').first())
