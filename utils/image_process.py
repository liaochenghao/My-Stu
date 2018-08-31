# coding: utf-8
import os
from rest_framework import exceptions
from PIL import Image
import logging
from StudentManageSys.settings import MEDIA_ROOT

logger = logging.getLogger("django")


class ImageProcess:
    @staticmethod
    def generate_agreement_pic(base_img_url, sign_img_url, user_id):
        if not os.path.exists(base_img_url):
            logger.info('File %s Not Exist' % base_img_url)
            raise exceptions.ValidationError('底图不存在')
        image = Image.open(base_img_url)
        sign_img_url = Image.open(sign_img_url)
        sign_img_url.thumbnail((60, 30))
        image.paste(sign_img_url, (410, 1380))
        relative_path = '%s%s%s' % ('agreement/', user_id, '_agreement.png')
        image_save_url = os.path.abspath(os.path.join(MEDIA_ROOT, relative_path))
        image.save(image_save_url)
        return relative_path
