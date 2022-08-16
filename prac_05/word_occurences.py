user_input = str(input("Text: "))
text = user_input.split()
length = 0
words = {}

for word in text:
    if len(word) > length:
        length = len(word)
    elif word in words:
        words[word] += 1
    else:
        words[word] = 1

for i in words:
    print(f"{i:10} : {words[i]}")



