# coding: utf-8
import base64
import uuid

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from StudentManageSys import settings
from order.models import Order
from student.functions import auto_assign_sales_man, change_student_status
from student.models import StudentInfo, StudentScoreDetail, StudentAgreement
from utils.image_process import ImageProcess
from utils.serializer_fields import VerboseChoiceField
import logging

logger = logging.getLogger('django')


class StudentInfoSerializer(serializers.ModelSerializer):
    gender = VerboseChoiceField(choices=StudentInfo.GENDER)
    card_img1 = Base64ImageField(required=False)
    card_img2 = Base64ImageField(required=False)
    transcript_img = Base64ImageField(required=False)

    # student_status = VerboseChoiceField(choices=StudentInfo.STUDENT_STATUS)

    class Meta:
        model = StudentInfo
        fields = ['id', 'name', 'birth_date', 'cschool', 'major', 'email', 'wechat', 'student_status', 'cc', 'server',
                  'first_name', 'phone', 'gender', 'birth_date', 'school_email', 'id_number', 'enrollment_year',
                  'student_number', 'gpa', 'cc_sign', 'server_sign', 'card_img1', 'card_img2', 'last_name', 'qr_code',
                  'transcript_img', 'intention', 'contact', 'contact_relation', 'contact_wechat', 'contact_email',
                  'modified_time', 'channel_id', 'channel_name', 'last_login', 'wechat_sign', 'sign_agreement',
                  'old_student']
        read_only_fields = ['openid', 'cc', 'server', 'student_status', 'qr_code', 'modified_time', 'channel_id',
                            'channel_name', 'last_login']

    def update(self, instance, validated_data):
        if not instance.cc:
            cc = auto_assign_sales_man(instance)
            validated_data['cc'] = cc
            validated_data['student_status'] = 'PERSONAL_FILE'
        if not instance.student_number and validated_data.get('student_number'):
            validated_data['student_status'] = 'COMPLETE_FILE'
        if not instance.transcript_img and validated_data.get('transcript_img'):
            validated_data['student_status'] = 'UPLOAD_FILE'
        if not instance.sign_agreement and validated_data.get('sign_agreement'):
            validated_data['student_status'] = 'SIGNED_AGREEMENT'

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # if self.context.get('request').query_params.get('all_payment_student'):
        #     data['payment_time'] = Order.
        return data


class StudentScoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentScoreDetail
        fields = ['id', 'user', 'country', 'region', 'city', 'address1', 'address2', 'post_code', 'recipient',
                  'recipient_phone']
        # read_only_fields = ['user']


class StudentAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAgreement
        fields = ['id', 'user_id', 'agreement', 'create_time']

    def create(self, validated_data):
        request = self.context.get('request')
        image_base64 = str(request.data['image']).replace('data:image/png;base64,', '')
        image_data = base64.b64decode(image_base64)
        abs_path = '%s/agreement/%s' % (settings.MEDIA_ROOT, str(uuid.uuid4()) + '.png')
        with open(abs_path, 'wb') as pic:
            pic.write(image_data)
        base_image_path = '%s%s' % (settings.MEDIA_ROOT, '/agreement/base.png')
        real_path = ImageProcess.generate_agreement_pic(base_image_path, abs_path, validated_data['user_id'].id)
        validated_data['agreement'] = real_path
        return super().create(validated_data)
