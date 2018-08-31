# Create your views here.
from rest_framework import mixins, viewsets
from channel.models import Channel
from channel.serializers import ChannelSerializer


class ChannelView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                  mixins.ListModelMixin):
    queryset = Channel.objects.all().filter()
    serializer_class = ChannelSerializer
