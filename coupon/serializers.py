import random
import string

from rest_framework import serializers

from coupon.models import Coupon, StudentCoupon


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'balance', 'start_at', 'end_at', 'type', 'total', 'create_time', 'update_time']

    def create(self, validated_data):
        validated_data['code'] = ''.join(random.sample(string.digits + string.ascii_uppercase, 10))
        return super().create(validated_data)


class StudentCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCoupon
        fields = ['id', 'user_id', 'coupon_id', 'coupon_expire_at', 'create_time']
