from django.contrib import admin

from .models import Loan, Payment


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    model = Loan
    list_display = (
        "value",
        "interest_rate",
        "created",
    )
    list_filter = (
        "bank",
        "client",
        "interest_rate",
    )
    search_fields = (
        "bank",
        "client",
    )
    ordering = ("-created",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = (
        "value",
        "loan",
        "created",
    )
    list_filter = ("loan",)
    search_fields = ("loan",)
    ordering = ("-created",)
