import unittest

from loan_logic import predict_loan_status


class TestLoanLogic(unittest.TestCase):

    def test_approved_loan(self):
        result = predict_loan_status(750, 0.20, "No")
        self.assertEqual(result, 1)

    def test_rejected_low_credit_score(self):
        result = predict_loan_status(600, 0.20, "No")
        self.assertEqual(result, 0)

    def test_rejected_previous_default(self):
        result = predict_loan_status(750, 0.20, "Yes")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
