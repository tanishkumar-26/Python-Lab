def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input())
num2 = int(input())

print(gcd(num1, num2))