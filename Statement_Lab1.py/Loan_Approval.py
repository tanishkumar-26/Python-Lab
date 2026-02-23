credit_score = int(input("Enter credit score: "))
monthly_income = float(input("Enter monthly income: "))
existing_loan = float(input("Enter existing loan amount: "))

if credit_score < 600:
    print("❌ Loan Rejected (Low Credit Score)")

elif 600 <= credit_score < 750:
    if monthly_income < 30000 and existing_loan > 50000:
        print("❌ Loan Rejected (Low income & High existing loan)")
    else:
        print("⏳ Loan Under Further Review")

else:  # credit_score >= 750
    if monthly_income < 30000 and existing_loan > 50000:
        print("❌ Loan Rejected (Low income & High existing loan)")
    else:
        print("✅ Loan Approved")