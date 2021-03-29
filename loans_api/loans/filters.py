import django_filters

from .models import Payment


class PaymentFilter(django_filters.FilterSet):
    created = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Payment
        fields = ("loan", "created")
