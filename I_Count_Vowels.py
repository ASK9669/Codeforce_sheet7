S = input()
vowels = "aeiouAEIOU"
count = 0
for char in S:
    if char in vowels:
        count += 1
print(count)   