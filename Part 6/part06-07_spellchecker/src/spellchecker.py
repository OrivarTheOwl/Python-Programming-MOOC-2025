user_input = input("Write text: ")
#user_input = "We use ptython to make a spell checker"

sentence = user_input.split()

final_words = []

all_words = []

with open ("wordlist.txt") as new_file:
    for line in new_file:
        all_words.append(line.strip())

for word in sentence:
    if word.lower() not in all_words:
        word = f"*{word}*"
    final_words.append(word)

new_sentence = " ".join(final_words)

print(new_sentence)