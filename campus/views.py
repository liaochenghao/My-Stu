# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from campus.models import Campus
from campus.serializers import CampusSerializer


class CampusView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    校区视图
    """
    queryset = Campus.objects.all().filter(is_active=True)
    serializer_class = CampusSerializer

    @list_route(['GET'])
    def all(self, request):
        return Response(Campus.objects.all().values('id', 'name'))
