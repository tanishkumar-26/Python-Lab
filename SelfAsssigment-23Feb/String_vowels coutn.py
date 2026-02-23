text = "programming"

vowels = "aeiou"
result = {}

for v in vowels:
    result[v] = text.count(v)

print(result)