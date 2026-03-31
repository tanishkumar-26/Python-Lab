ch = input("Enter character: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Invalid Input")