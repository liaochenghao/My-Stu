# coding: utf-8
import qrcode
from urllib import parse
from StudentManageSys.settings import DOMAIN, WX_CONFIG, MEDIA_ROOT


def make_qrcode(channel_id):
    """
    根据渠道编号生成对应的图片二维码
    :param channel_id:
    :return:
    """
    redirect_uri = parse.quote('%s/?channel_id=%s' % (DOMAIN, channel_id))
    channel_url = """https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_base&state=STATE#wechat_redirect""" % (
        WX_CONFIG['APP_ID'], redirect_uri)
    channel_img = qrcode.make(channel_url)
    qr_code_save_path = '%s%s%s%s' % (MEDIA_ROOT, '/channel/channel_', channel_id, '.jpg')
    qr_code_url = '%s%s%s%s%s' % (DOMAIN, 'media', '/channel/channel_', channel_id, '.jpg')
    channel_img.save(qr_code_save_path)
    return qr_code_url, channel_url
