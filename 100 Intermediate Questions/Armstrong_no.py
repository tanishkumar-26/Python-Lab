n = int(input("Enter number: "))
temp = n
sum_power = 0
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    sum_power += digit ** digits
    temp //= 10

if sum_power == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")