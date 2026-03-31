def is_armstrong(n):
    power = len(str(n))
    total = sum(int(digit) ** power for digit in str(n))
    return total == n


n = int(input("Enter number: "))
print("Result:", is_armstrong(n))