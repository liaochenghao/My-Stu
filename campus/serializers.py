from rest_framework import serializers

from campus.models import Campus


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ['id', 'name', 'info', 'create_time', 'update_time']
