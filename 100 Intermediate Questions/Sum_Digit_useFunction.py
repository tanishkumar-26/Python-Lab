def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

num = int(input())
print(sum_of_digits(num))