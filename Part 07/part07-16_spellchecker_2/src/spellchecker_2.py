from difflib import get_close_matches

user_input = input("write text: ")
#user_input = "We use ptython to make a spell checker"

sentence = user_input.split()
final_sentence = []
all_words = []
misspelled_words = []

with open ("wordlist.txt") as new_file:
    for line in new_file:
        all_words.append(line.strip())

for word in sentence:
    if word.lower() not in all_words:
        misspelled_words.append(word)
        word = f"*{word}*"
    final_sentence.append(word)
new_sentence = " ".join(final_sentence)

print(new_sentence)

print("suggestions:")
for word in misspelled_words:
    close_words = get_close_matches(word, all_words)
    close_options = ', '.join(close_words)
    print(f"{word}: {close_options}")

