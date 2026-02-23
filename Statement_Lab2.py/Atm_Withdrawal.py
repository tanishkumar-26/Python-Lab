balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

daily_limit = 50000

if withdraw_amount > daily_limit:
    print("❌ Exceeds daily withdrawal limit (₹50,000)")
elif withdraw_amount > balance:
    print("❌ Insufficient account balance")
elif withdraw_amount > atm_cash:
    print("❌ ATM does not have sufficient cash")
else:
    balance -= withdraw_amount
    print("✅ Withdrawal Successful")
    print("Remaining Balance: ₹", balance)