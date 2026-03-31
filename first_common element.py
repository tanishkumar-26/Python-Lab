# Count frequency of characters

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# Input
s = input("Enter a string: ")

# Output
result = char_frequency(s)
print("Character frequency:", result)