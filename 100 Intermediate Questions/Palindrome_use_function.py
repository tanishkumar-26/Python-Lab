def is_palindrome(s):
    return s == s[::-1]

text = input()

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")