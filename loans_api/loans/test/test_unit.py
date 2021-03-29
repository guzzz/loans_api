from datetime import date
from django.db.utils import IntegrityError
from django.test import TestCase

from loans_api.users.models import CustomUser

from ..models import Loan, Payment


class LoanUnitTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(LoanUnitTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING Loan UNIT Tests...")
        print("======================================================================")
        print("... CREATING initial configuration ..............................")

        initial_user = CustomUser.objects.create(
            email="klose@email.com", password="cash1234"
        )

        print("----------------------------------------------------------------------")

    def test_create_new_loan(self):
        print("==> Creating NEW loan")
        try:
            new_loan = Loan.objects.create(
                value="1000.00",
                interest_rate="0.1",
                ip_address="127.168.0.1",
                bank="Itau",
                client="Seu José",
                user=CustomUser.objects.all().first(),
                created=date.today(),
            )
            self.assertEqual(type(new_loan), Loan)
            self.assertEqual(
                str(new_loan), f"Empréstimo de $1000.00 criado em {date.today()}"
            )
        except:
            self.assertEqual(False, True)
        print("----------------------------------------------------------------------")


class PaymentUnitTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(PaymentUnitTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING Payment UNIT Tests...")
        print("======================================================================")
        print("... CREATING initial configuration ..............................")

        initial_user = CustomUser.objects.create(
            email="klose@email.com", password="cash1234"
        )

        initial_loan = Loan.objects.create(
            value="1000.00",
            interest_rate="0.1",
            ip_address="127.168.0.1",
            bank="Itau",
            client="Seu José",
            user=initial_user,
            created=date.today(),
        )
        print("----------------------------------------------------------------------")

    def test_create_new_payment(self):
        print("==> Creating NEW payment")
        try:
            new_payment = Payment.objects.create(
                value="1000.00",
                loan=Loan.objects.all().first(),
                created=date.today(),
            )
            self.assertEqual(type(new_payment), Payment)
            self.assertEqual(str(new_payment), f"Pagamento de $1000.00")
        except:
            self.assertEqual(False, True)
        print("----------------------------------------------------------------------")
