# Check Armstrong number

def is_armstrong(n):
    power = len(str(n))
    return sum(int(d)**power for d in str(n)) == n


# Input
n = int(input("Enter number: "))

# Output
print("Is Armstrong:", is_armstrong(n))