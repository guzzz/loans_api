from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework_extensions.mixins import DetailSerializerMixin

from .models import Loan, Payment
from .filters import PaymentFilter
from .filter_backends import PaymentFilterBackend
from .serializers import LoanSerializer, LoanEditSerializer, PaymentSerializer


class LoanModelViewSet(
    DetailSerializerMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet,
):

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    serializer_detail_class = LoanEditSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(user__id=self.request.user.id)
        return queryset


class PaymentModelViewSet(
    CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet
):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_class = PaymentFilter
    filter_backends = (PaymentFilterBackend,)

    def get_queryset(self):
        queryset = self.queryset.filter(loan__user__id=self.request.user.id)
        return queryset
