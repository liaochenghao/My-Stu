# Create your views here.
import base64
import uuid

from django.db import transaction
from rest_framework import mixins, viewsets, exceptions, serializers
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.views import APIView

from StudentManageSys import settings
from authentication.function import generate_token
from log_info.opration_type import UserOperationType
from user_info.function import generate_menu_tree, decorate_menu_tree, md5
from user_info.models import Department, Role, Privilege, Menu, UserInfo
from user_info.serializers import DepartmentSerializer, RoleSerializer, PrivilegeSerializer, MenuSerializer, \
    UserInfoSerializer
from user_info.tasks import add
from utils.common import log_to_db, get_ip_address
import logging

logger = logging.getLogger('django')


class DepartmentView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                     mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Department.objects.filter(enabled=True).all()
    serializer_class = DepartmentSerializer
    filter_fields = ['name']

    @list_route(['GET'])
    def all(self, request):
        return Response(Department.objects.all().values('id', 'name'))


class RoleView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
               mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Role.objects.filter(enabled=True).all()
    serializer_class = RoleSerializer
    filter_fields = ['name']

    @list_route(['GET'])
    def all(self, request):
        return Response(Role.objects.all().values('id', 'name'))


class PrivilegeView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer

    @list_route(['GET'])
    def get_current_privilege(self, request):
        param = request.query_params
        role_id = param.get('role_id')
        if not role_id:
            raise exceptions.ValidationError('参数role_id为空')
        current_menu = Privilege.objects.filter(role_id=role_id).values_list('menu_id')
        current_menu_id_list = [menu[0] for menu in current_menu]
        result = MenuSerializer(Menu.objects.all().order_by('id'), many=True).data
        json_tree = generate_menu_tree(result[1:], result[0])
        full_tree = json_tree['children']
        decorate_menu_tree(full_tree, current_menu_id_list)
        return Response(full_tree)

    @list_route(['POST'])
    @transaction.atomic()
    def set_current_privilege(self, request):
        param = request.data
        role_id = param.get('role_id')
        menu_id_list = param.get('menu_id_list')
        if not role_id:
            raise exceptions.ValidationError('参数role_id为空')
        current_menu = Privilege.objects.filter(role_id=role_id).values_list('menu_id')
        current_menu_id_list = [menu[0] for menu in current_menu]
        add_menu_list = [_id for _id in menu_id_list if _id not in current_menu_id_list]
        del_menu_list = [_id for _id in current_menu_id_list if _id not in menu_id_list]
        if len(add_menu_list) > 0:
            role = Role.objects.filter(id=role_id).first()
            add_menu_object = [Privilege(role_id=role, menu_id=Menu.objects.filter(id=menu_id).first()) for menu_id in
                               add_menu_list]
            Privilege.objects.bulk_create(add_menu_object)
        if len(del_menu_list) > 0:
            Privilege.objects.filter(menu_id__in=del_menu_list).delete()
        return Response()


class MenuView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @list_route(['GET'])
    def get_menu_tree(self, request):
        log_to_db(operator='1', operation=1, ip_address=get_ip_address(request), description='fwef', operator_type=1)
        result = MenuSerializer(Menu.objects.all().order_by('id'), many=True).data
        json_tree = generate_menu_tree(result[1:], result[0])
        return Response(json_tree['children'])


class UserInfoView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin):
    queryset = UserInfo.objects.filter(active=True).all()
    serializer_class = UserInfoSerializer
    filter_fields = ['name', 'username']

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        is_leader = False
        if 'is_leader' in request.data.keys():
            leader = request.data.pop('is_leader')
            is_leader = True if leader == 'true' else False
        request.data['password'] = md5('123456')
        qr_code = request.data.get('qr_code')
        if qr_code:
            image_base64 = str(qr_code)[str(qr_code).find(',') + 1:]
            image_data = base64.b64decode(image_base64)
            file_name = str(uuid.uuid4()) + '.' + str(qr_code)[str(qr_code).find('/') + 1:str(qr_code).find(';')]
            abs_path = '%s/images/user_qrcode/%s' % (settings.MEDIA_ROOT, file_name)
            with open(abs_path, 'wb') as pic:
                pic.write(image_data)
            request.data['qr_code'] = 'images/user_qrcode/%s' % file_name
        department = Department.objects.filter(id=request.data['department_id']).first()
        request.data['department_name'] = department.name
        role = Role.objects.filter(id=request.data['role_id']).first()
        request.data['role_name'] = role.name
        result = super().create(request, *args, **kwargs)
        if is_leader:
            department.leader_id = result.data['id']
            department.leader_name = result.data['name']
            department.save()
        log_to_db(operator=result.data['id'], operation=UserOperationType.UPDATE_INFO.value,
                  ip_address=get_ip_address(request))
        return result

    @list_route(['POST'])
    def check_url(self, request):
        params = request.data
        visit_url = params.get('visit_url')
        if not visit_url:
            raise serializers.ValidationError('visit_url为空')
        # 获取当前用户的角色，并查找到对应的菜单访问权限进行判断
        return Response()

    @list_route(['PUT'])
    @transaction.atomic()
    def basic_info_update(self, request):
        params = request.data
        user_id = params.get('id')
        if not user_id:
            raise serializers.ValidationError('user_id为空')
        is_leader = None
        if 'is_leader' in params.keys():
            is_leader = params.pop('is_leader')
        if 'qr_code' in params.keys():
            qr_code = params.pop('qr_code')
            image_base64 = str(qr_code)[str(qr_code).find(',') + 1:]
            image_data = base64.b64decode(image_base64)
            file_name = str(uuid.uuid4()) + '.' + str(qr_code)[str(qr_code).find('/') + 1:str(qr_code).find(';')]
            abs_path = '%s/images/user_qrcode/%s' % (settings.MEDIA_ROOT, file_name)
            with open(abs_path, 'wb') as pic:
                pic.write(image_data)
            params['qr_code'] = 'images/user_qrcode/' + file_name
        UserInfo.objects.filter(id=user_id).update(**params)
        data = UserInfo.objects.filter(id=user_id).first()
        if is_leader:
            Department.objects.filter(id=data.department_id.id).update(leader_id=data.id, leader_name=data.name)
        log_to_db(operator=user_id, operation=UserOperationType.UPDATE_INFO.value,
                  ip_address=get_ip_address(request), description='修改用户信息', operator_type=1)
        return Response()

    @list_route(['POST'])
    def login(self, request):
        params = request.data
        username = params.get('username')
        password = params.get('password')
        if not all((username, password)):
            raise serializers.ValidationError('用户名和密码不能为空')
        result = UserInfo.objects.filter(username=username, password=password).values('id').first()
        if result:
            token_data = generate_token(result['id'], 0)
            response = Response()
            response.setdefault('token', token_data)
            response['Access-Control-Expose-Headers'] = 'token'
            log_to_db(operator=result['id'], operation=UserOperationType.LOGIN.value,
                      ip_address=get_ip_address(request), description='登录系统', operator_type=1)
            return response
        else:
            raise serializers.ValidationError('用户名或密码验证失败')

    @list_route(['GET'])
    def cc_list(self, request):
        result = UserInfo.objects.filter(department_name='销售部')
        return Response(UserInfoSerializer(result, many=True).data)


class TestView(APIView):

    def get(self, request):
        add.delay(5, 6)
        return Response()
