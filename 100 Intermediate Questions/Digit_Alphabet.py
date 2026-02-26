ch = input("Enter character: ")

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special Character")