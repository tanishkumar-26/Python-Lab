num = int(input("Enter number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

if start <= num <= end:
    print("Number lies within range")
else:
    print("Number does not lie within range")