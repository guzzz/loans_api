from rest_framework import serializers

from .models import Loan, Payment
from .fields import CurrentIpAddress, CurrentUser
from .services import LoanBalanceService


class LoanSerializer(serializers.ModelSerializer):
    ip_address = serializers.HiddenField(default=CurrentIpAddress())
    user = serializers.HiddenField(default=CurrentUser())

    class Meta:
        model = Loan
        fields = (
            "id",
            "value",
            "interest_rate",
            "ip_address",
            "bank",
            "client",
            "user",
            "created",
        )


class LoanEditSerializer(serializers.ModelSerializer):
    outstanding_balance = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = (
            "value",
            "interest_rate",
            "ip_address",
            "bank",
            "client",
            "outstanding_balance",
            "created",
        )

    def get_outstanding_balance(self, obj):
        return LoanBalanceService.calculate_outstanding_balance(
            str(obj.id), obj.value, obj.interest_rate, obj.created
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
