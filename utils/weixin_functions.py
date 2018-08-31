# coding: utf-8
import datetime
import json
import logging
import random
import requests
from rest_framework import exceptions

from StudentManageSys.settings import WX_CONFIG
from authentication.function import generate_token
from student.models import StudentInfo
from user_info.models import UserInfo
from utils.redis_server import redis_client

logger = logging.getLogger('django')


class WxInterface:
    def __init__(self):
        self.appid = WX_CONFIG['APP_ID']
        self.secret = WX_CONFIG['APP_SECRET']

    # 微信公众号code认证
    def code_authorize(self, code):
        # url = "https://api.weixin.qq.com/sns/jscode2session"
        # params = {
        #     'appid': self.appid,
        #     'secret': self.secret,
        #     'js_code': code,
        #     'grant_type': 'authorization_code'
        # }
        # response = requests.get(url=url, params=params, verify=False)
        # if response.status_code != 200:
        #     logger.info('X' * 70)
        #     logger.info(response.text)
        #     logger.info('X' * 70)
        #     raise exceptions.ValidationError('连接微信服务器异常')
        # res = response.json()
        # if res.get('openid'):
        #     # 首先查询数据库中是否存在该用户信息
        #     user_info = StudentInfo.objects.filter(openid=res['openid']).first()
        #     if not user_info:
        #         # 给用户生成邀请码
        #         # while True:
        #         #     seed = random.random()
        #         #     code = str(int(seed * 1000000))
        #         #     code = code + '8' * (6 - len(code)) if len(code) < 6 else code
        #         #     code_exist = UserInfo.objects.filter(code=code).count()
        #         #     if code_exist == 0:
        #         #         break
        #         # qr_code = self.get_forever_qrcode(res.get('openid'))
        #         # 如果用户不存在，则向数据库插入数据
        #         user_info = StudentInfo.objects.create(openid=res['openid'], last_login=datetime.datetime.now())
        #     else:
        #         # 如果用户存在，更新用户信息
        #         user_info.last_login = datetime.datetime.now()
        #         user_info.save()
        #     token = generate_token(user_info.id, 1)
        #     return {'user_id': user_info.id, 'token': token}
        # else:
        #     logger.info('X' * 70)
        #     logger.info(response.text)
        #     logger.info('X' * 70)
        #     raise exceptions.ValidationError('微信认证异常： %s' % json.dumps(res))
        user_info = StudentInfo.objects.filter(id=4).first()
        token = generate_token(user_info.id, 1)
        return {'user_id': user_info.id, 'token': token}

    def get_grant_token(self):
        # access_token是公众号的全局唯一接口调用凭据，公众号调用各接口时都需使用access_token。
        # 开发者需要进行妥善保存。access_token的存储至少要保留512个字符空间。access_token的有
        # 效期目前为2个小时，需定时刷新，重复获取将导致上次获取的access_token失效。
        """获取微信access_token"""
        access_token = redis_client.get_instance('%s_access_token' % self.appid)
        if access_token:
            return access_token
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
            self.appid, self.secret)
        response = requests.get(url)
        res_data = response.json()
        redis_client.set_instance('%s_access_token' % self.appid, res_data['access_token'],
                                  default_valid_time=(2 * 60 * 60 - 100))
        return res_data['access_token']


WxInterfaceUtil = WxInterface()
