def predict_loan_status(credit_score, loan_percent_income, previous_loan_defaults):
    """
    Simple loan approval decision rule used for CI testing.
    Returns 1 for approved and 0 for rejected.
    """

    if (
        credit_score >= 650
        and loan_percent_income <= 0.40
        and previous_loan_defaults == "No"
    ):
        return 1
    else:
        return 0


if __name__ == "__main__":
    result = predict_loan_status(750, 0.20, "No")
    print("Predicted Loan Status:", result)
