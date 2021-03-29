import json
from datetime import date
from rest_framework.test import APITestCase

from loans_api.users.models import CustomUser

from ..models import Loan, Payment


class LoanIntegrationTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(LoanIntegrationTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING Loan INTEGRATION Tests...")
        print("======================================================================")
        print("... CREATING initial configuration ..............................")

        user_instance = CustomUser.objects.create(email="drogba@email.com")
        user_instance.set_password("loans1234")
        user_instance.save()

        initial_loan = Loan.objects.create(
            value="1000.00",
            interest_rate="0.1",
            ip_address="127.168.0.1",
            bank="Itau",
            client="Seu José",
            user=user_instance,
            created=date.today(),
        )

        print("----------------------------------------------------------------------")

    def setUp(self):
        response = self.client.post(
            "/api/token/", {"email": "drogba@email.com", "password": "loans1234"}
        )
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + response.data["access"])

    def test_list_loans(self):
        print("==> LIST: [GET] /loans/")
        response = self.client.get("/loans/")
        self.assertEqual(response.status_code, 200)
        print("----------------------------------------------------------------------")

    def test_retrieve_loan_not_payd(self):
        print("==> LIST: [GET] /loans/ID/")
        loan_id = str(Loan.objects.all().first().id)
        response = self.client.get(f"/loans/{loan_id}/")
        self.assertEqual(response.status_code, 200)
        print("----------------------------------------------------------------------")

    def test_retrieve_loan_partial_payd(self):
        print("==> LIST: [GET] /loans/ID/")
        loan = Loan.objects.all().first()

        initial_payment = Payment.objects.create(
            value="1000.00",
            loan=loan,
            created=date.today(),
        )
        response = self.client.get(f"/loans/{loan.id}/")
        self.assertEqual(response.status_code, 200)
        print("----------------------------------------------------------------------")

    def test_create_loan(self):
        print("==> CREATE: [POST] /loans/")
        data = {
            "value": "1500.00",
            "interest_rate": "0.1",
            "bank": "Itau",
            "client": "Seu Zé",
            "created": "2021-03-28",
        }
        response = self.client.post(
            "/loans/", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        print("----------------------------------------------------------------------")


class PaymentIntegrationTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(PaymentIntegrationTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING Payment INTEGRATION Tests...")
        print("======================================================================")
        print("... CREATING initial configuration ..............................")

        user_instance = CustomUser.objects.create(email="ibra@email.com")
        user_instance.set_password("loans1234")
        user_instance.save()

        initial_loan = Loan.objects.create(
            value="1000.00",
            interest_rate="0.1",
            ip_address="127.168.0.1",
            bank="Itau",
            client="Seu José",
            user=user_instance,
            created=date.today(),
        )

        initial_payment = Payment.objects.create(
            value="1000.00",
            loan=initial_loan,
            created=date.today(),
        )

        print("----------------------------------------------------------------------")

    def setUp(self):
        response = self.client.post(
            "/api/token/", {"email": "ibra@email.com", "password": "loans1234"}
        )
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + response.data["access"])

    def test_list_payments(self):
        print("==> LIST: [GET] /payments/")
        response = self.client.get("/payments/")
        self.assertEqual(response.status_code, 200)
        print("----------------------------------------------------------------------")

    def test_retrieve_payment(self):
        print("==> LIST: [GET] /payments/ID/")
        payment_id = str(Payment.objects.all().first().id)
        response = self.client.get(f"/payments/{payment_id}/")
        self.assertEqual(response.status_code, 200)
        print("----------------------------------------------------------------------")

    def test_create_payment(self):
        print("==> CREATE: [POST] /payments/")
        loan_id = str(Loan.objects.all().first().id)
        data = {"value": "1500.00", "loan": loan_id, "created": "2021-03-28"}
        response = self.client.post(
            "/payments/", data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        print("----------------------------------------------------------------------")
