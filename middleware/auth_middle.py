# coding: utf-8
import json

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

# from user_info.models import UserInfo

import logging

from StudentManageSys.settings import ignore_auth_urls
from student.models import StudentInfo
from authentication.function import refresh_token, token_auth
from user_info.models import UserInfo

logger = logging.getLogger("django")


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        url_path = request.path
        if url_path in ignore_auth_urls:
            return
        logger.info('Auth Url ---------------------------> %s' % (request.method + ':  ' + url_path))
        # token = request.META.get('HTTP_X_AUTH_TOKEN')
        # if not token:
        #     return HttpResponse(content=json.dumps(dict(code=400, msg='请在请求头中带好你的token')),
        #                         content_type='application/json')
        # try:
        #     user_id, is_student, is_refresh = token_auth(token)
        # except Exception as e:
        #     return HttpResponse(content=json.dumps(dict(code=401, msg=e.__str__()), content_type='application/json'))
        # request.refresh_token = is_refresh
        # if is_student == 1:
        #     user = StudentInfo.objects.first()
        # else:
        #     user = UserInfo.objects.first()
        # request.user = user
        # request.is_student = is_student

        user = StudentInfo.objects.filter(id=4).first()
        request.user = user

    def process_response(self, request, response):
        return response
        # url_path = request.path
        # if url_path in ignore_auth_urls:
        #     return
        # if request.refresh_token:
        #     user = request.user
        #     token = refresh_token(user.id, request.is_student)
        #     logger.info('Refresh Token ---------> %s' % (request.method + ':  ' + url_path))
        #     response['token'] = token
        # return response
