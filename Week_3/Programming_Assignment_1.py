words = input().split(',')

longest_word = ""
max_length = 0

for word in words:
    if len(word) >= max_length:
        longest_word = word
        max_length = len(word)

print(longest_word)
