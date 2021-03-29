import uuid
from django.db import models


class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.DecimalField(max_digits=16, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=6, decimal_places=2)
    ip_address = models.GenericIPAddressField(protocol="both", unpack_ipv4=True)
    bank = models.TextField()
    client = models.TextField()
    user = models.ForeignKey(
        to="users.CustomUser",
        related_name="%(class)s",
        null=False,
        on_delete=models.CASCADE,
    )
    created = models.DateField()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Empréstimo de ${self.value} criado em {self.created}"


class Payment(models.Model):
    value = models.DecimalField(max_digits=16, decimal_places=2)
    loan = models.ForeignKey(
        to=Loan, related_name="%(class)s", null=False, on_delete=models.CASCADE
    )
    created = models.DateField()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Pagamento de ${self.value}"


class PaymentsByLoanDBView(models.Model):
    id = models.BigIntegerField(primary_key=True)
    loan = models.CharField(max_length=32)
    total_payd = models.DecimalField(max_digits=16, decimal_places=2)

    class Meta:
        managed = False
        db_table = "payments_by_loan_db_view"
