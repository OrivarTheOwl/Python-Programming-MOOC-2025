sentence = []

while True:
    word = input("Word: ")
    if word in sentence:
        break
    else:
        sentence.append(word)

print(f"You typed in {len(sentence)} different words")