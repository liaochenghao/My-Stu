# coding: utf-8
import datetime

from rest_framework import serializers
from user_info.models import Department, Role, Privilege, Menu, UserInfo

import logging

from utils.common import append_url_with_domain, datetime_format

logger = logging.getLogger('django')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'leader_id', 'leader_name', 'create_at', 'update_at', 'enabled']

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['create_at'] = datetime_format(data['create_at'])
    #     return data


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'create_at', 'update_at', 'enabled']

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['create_at'] = datetime_format(data['create_at'])
    #     return data


class PrivilegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privilege
        fields = ['id', 'role_id', 'menu_id', 'extra', 'create_at']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'url', 'parent_id', 'extra', 'create_at']


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'role_id', 'role_name', 'name', 'email', 'phone', 'sex', 'department_id',
                  'department_name', 'active', 'qr_code', 'create_time', 'update_time', 'password', 'wechat',
                  'leader_id', 'leader_name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get('qr_code'):
            data['qr_code'] = append_url_with_domain(data['qr_code'])
        data.pop('password')
        data['is_leader'] = True if Department.objects.filter(leader_id=data['id']).count() > 0 else False
        if data['leader_id'] != -1:
            leader = UserInfo.objects.filter(id=data['leader_id']).first()
            if leader:
                data['leader_name'] = leader.name
        return data
