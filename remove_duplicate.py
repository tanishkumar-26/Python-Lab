# First non-repeating character

def first_non_repeating(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


# Input
s = input("Enter string: ")

# Output
print("First non-repeating character:", first_non_repeating(s))