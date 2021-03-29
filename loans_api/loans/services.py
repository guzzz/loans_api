import pytz
from decimal import Decimal
from datetime import date
from dateutil import relativedelta

from .models import PaymentsByLoanDBView


class LoanBalanceService:
    @staticmethod
    def calculate_months_period(loan_created) -> int:
        today = date.today()
        dates_difference = relativedelta.relativedelta(today, loan_created)
        total_months = int(dates_difference.months + (12 * dates_difference.years))
        return total_months

    @staticmethod
    def calculate_total_debit(loan_value, loan_interest_rate, loan_created) -> Decimal:
        total_months = LoanBalanceService.calculate_months_period(loan_created)
        total_value = Decimal(
            loan_value * ((1 + loan_interest_rate / 100) ** total_months)
        )
        return total_value

    @staticmethod
    def calculate_outstanding_balance(
        loan_id, loan_value, loan_interest_rate, loan_created
    ) -> str:
        total_debt = LoanBalanceService.calculate_total_debit(
            loan_value, loan_interest_rate, loan_created
        )
        payments_sum = PaymentsByLoanDBView.objects.filter(loan=loan_id).first()
        if payments_sum:
            already_payd = payments_sum.total_payd
            outstanding_balance = total_debt - already_payd
            outstanding_balance = "{:.2f}".format(outstanding_balance)
        else:
            outstanding_balance = "{:.2f}".format(total_debt)
        return outstanding_balance
