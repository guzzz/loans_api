# Generated by Django 3.1 on 2021-03-28 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentsByLoanDBView",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("loan", models.CharField(max_length=32)),
                ("total_payd", models.DecimalField(decimal_places=2, max_digits=16)),
            ],
            options={
                "db_table": "payments_by_loan_db_view",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=16)),
                ("interest_rate", models.DecimalField(decimal_places=2, max_digits=6)),
                ("ip_address", models.GenericIPAddressField(unpack_ipv4=True)),
                ("bank", models.TextField()),
                ("client", models.TextField()),
                ("created", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="loan",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=16)),
                ("created", models.DateField()),
                (
                    "loan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to="loans.loan",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
    ]
