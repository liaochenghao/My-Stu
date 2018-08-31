# Create your views here.
import base64
import uuid

from rest_framework import mixins, viewsets

from StudentManageSys import settings
from complain.models import Complain
from complain.serializers import ComplainSerializer


class ComplainView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                   mixins.ListModelMixin):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer

    def create(self, request, *args, **kwargs):
        picture = request.data.get('picture')
        image_base64 = str(picture)[str(picture).find(',') + 1:]
        image_data = base64.b64decode(image_base64)
        file_name = str(uuid.uuid4()) + '.' + str(picture)[str(picture).find('/') + 1:str(picture).find(';')]
        abs_path = '%s/images/complain/%s' % (settings.MEDIA_ROOT, file_name)
        with open(abs_path, 'wb') as pic:
            pic.write(image_data)
        request.data['picture'] = 'images/complain/%s' % file_name
        return super().create(request, *args, **kwargs)
