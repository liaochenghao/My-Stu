from rest_framework import serializers

from payment.models import PaymentAccountInfo


class PaymentAccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAccountInfo
        fields = ['id', 'account_number', 'account_name', 'opening_bank', 'payment', 'currency', 'create_time',
                  'swift_code', 'routing_number_paper', 'routing_number_wires', 'swift_code_foreign_currency',
                  'company_address', 'pay_link']