# Create your views here.
from rest_framework import viewsets, mixins

from log_info.models import OperationLog
from log_info.serializers import OperationLogSerializer


class OperationLogView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = OperationLog.objects.all().filter()
    serializer_class = OperationLogSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        param = self.request.query_params
        queryset = queryset.filter(**param)
        return queryset
