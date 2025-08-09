message = input()
vowels = "aeiouAEIOU"
count = 0
for char in message:
  if char in vowels:
    count += 1
print(count)
