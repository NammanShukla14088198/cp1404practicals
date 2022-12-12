"""
CP1404 Practical
Word Occurrence
"""
count = {}
userInput = input("Enter your sentence: ")
words = userInput.split()

for word in words:
    frequency = count.get(word, 0)
    count[word] = frequency + 1


words = list(count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {count[word]}")




