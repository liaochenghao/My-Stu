# Create your views here.
from rest_framework import mixins, viewsets

from message.models import StudentMessage
from message.serializers import StudentMessageSerializer


class StudentMessageView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet, mixins.UpdateModelMixin):
    queryset = StudentMessage.objects.all()
    serializer_class = StudentMessageSerializer
    filter_fields = ['student']
