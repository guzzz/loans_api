import json
from datetime import date
from rest_framework.test import APITestCase

from loans_api.users.models import CustomUser

from ..models import Loan, Payment
from .requests import *


class CustomTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(CustomTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING CUSTOM Tests...")
        print("======================================================================")
        print("... CREATING initial configuration ..............................")

        user_instance = CustomUser.objects.create(email="vinijr@email.com")
        user_instance.set_password("loans1234")
        user_instance.save()

        print("----------------------------------------------------------------------")

    def setUp(self):
        response = self.client.post(
            "/api/token/", {"email": "vinijr@email.com", "password": "loans1234"}
        )
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + response.data["access"])

    def test_custom_1(self):
        response = self.client.post(
            "/loans/", data=json.dumps(LOAN_1), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

        loan_id = response.data.get("id")

        LOAN_1_PAYMENT_1.update({"loan": loan_id})
        LOAN_1_PAYMENT_2.update({"loan": loan_id})
        LOAN_1_PAYMENT_3.update({"loan": loan_id})

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_1_PAYMENT_1),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_1_PAYMENT_2),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_1_PAYMENT_3),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f"/loans/{loan_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("outstanding_balance"), "28578.05")
        print("----------------------------------------------------------------------")

    def test_custom_2(self):
        response = self.client.post(
            "/loans/", data=json.dumps(LOAN_2), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

        loan_id = response.data.get("id")

        LOAN_2_PAYMENT_1.update({"loan": loan_id})
        LOAN_2_PAYMENT_2.update({"loan": loan_id})

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_2_PAYMENT_1),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_2_PAYMENT_2),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f"/loans/{loan_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("outstanding_balance"), "2147.51")
        print("----------------------------------------------------------------------")

    def test_custom_3(self):
        response = self.client.post(
            "/loans/", data=json.dumps(LOAN_3), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

        loan_id = response.data.get("id")

        LOAN_3_PAYMENT_1.update({"loan": loan_id})
        LOAN_3_PAYMENT_2.update({"loan": loan_id})
        LOAN_3_PAYMENT_3.update({"loan": loan_id})
        LOAN_3_PAYMENT_4.update({"loan": loan_id})
        LOAN_3_PAYMENT_5.update({"loan": loan_id})

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_3_PAYMENT_1),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_3_PAYMENT_2),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_3_PAYMENT_3),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_3_PAYMENT_4),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/payments/",
            data=json.dumps(LOAN_3_PAYMENT_5),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f"/loans/{loan_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("outstanding_balance"), "997570.64")
        print("----------------------------------------------------------------------")
