"""실행: python -m unittest discover -s tests -v"""

import unittest
from decimal import Decimal

from fastapi.testclient import TestClient

from main import app, calculate


class CalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_home_and_css(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('name="first"', response.text)
        self.assertIn('name="second"', response.text)
        self.assertEqual(self.client.get("/static/style.css").status_code, 200)

    def test_four_operations(self):
        response = self.client.post("/calculate", data={"first": "12", "second": "4"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual([r["value"] for r in response.context["results"]], ["16", "8", "48", "3"])

    def test_decimal_precision(self):
        results = calculate(Decimal("0.1"), Decimal("0.2"))
        self.assertEqual([r["value"] for r in results], ["0.3", "-0.1", "0.02", "0.5"])

    def test_negative_and_whitespace(self):
        response = self.client.post("/calculate", data={"first": " -12.5 ", "second": ".5"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual([r["value"] for r in response.context["results"]], ["-12", "-13", "-6.25", "-25"])

    def test_zero_divisor(self):
        for zero in ("0", "-0.000"):
            with self.subTest(zero=zero):
                response = self.client.post("/calculate", data={"first": "5", "second": zero})
                self.assertEqual(response.status_code, 200)
                self.assertEqual([r["value"] for r in response.context["results"]], ["5", "5", "0", "0으로 나눌 수 없습니다."])

    def test_invalid_inputs(self):
        for value in ("", "abc", "NaN", "Infinity", "1e999", "1,000", "1_000", "9" * 16, "0.12345678901"):
            for field in ("first", "second"):
                with self.subTest(value=value, field=field):
                    data = {"first": "2", "second": "3", field: value}
                    response = self.client.post("/calculate", data=data)
                    self.assertEqual(response.status_code, 400)
                    self.assertIn('role="alert"', response.text)
                    self.assertEqual(response.context["results"], [])

    def test_missing_fields(self):
        self.assertEqual(self.client.post("/calculate", data={}).status_code, 400)

    def test_rounding(self):
        self.assertEqual(calculate(Decimal("1"), Decimal("3"))[-1]["value"], "0.3333333333")
        self.assertEqual(calculate(Decimal("2"), Decimal("3"))[-1]["value"], "0.6666666667")

    def test_limits(self):
        response = self.client.post("/calculate", data={"first": "999999999999999.9999999999", "second": "0.0000000001"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["results"][-1]["value"], "9999999999999999999999999")
        number = Decimal("999999999999999.9999999999")
        self.assertEqual(calculate(number, number)[2]["value"], "999999999999999999999999800000.00000000000000000001")

    def test_html_is_escaped(self):
        response = self.client.post("/calculate", data={"first": '<script>alert("x")</script>', "second": "2"})
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('<script>', response.text)
        self.assertIn("&lt;script&gt;", response.text)


if __name__ == "__main__":
    unittest.main()
