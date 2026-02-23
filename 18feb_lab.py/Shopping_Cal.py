# Shopping Bill Calculation

notebooks = 3
notebook_price = 45

pens = 2
pen_price = 20

# Total bill
total_bill = (notebooks * notebook_price) + (pens * pen_price)

print("Total Bill Amount =", total_bill)

# Remaining balance if customer gives 500
given_amount = 500
remaining_balance = given_amount - total_bill

print("Remaining Balance =", remaining_balance)