import random
from random_word import list_of_random_words

word = random.choice(list_of_random_words)

word_list = []

for item in word:

    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())

already_checked_list = []
final_msg = None

count_lives = 1
while count_lives <= 7:
    if "".join(word_list) == word:
        final_msg = "Congrats! " + word
        break
    user_letter = input("Alege o litera: ").lower()
    if user_letter == "":
        print("Introdu o litera")
        continue
    elif user_letter in word_list:
        print("Litera deja afisata pe ecran")
        print(" ".join(word_list))
    elif user_letter in already_checked_list:
        print(f"Litera deja incercata. Litere incercate: {', '.join(already_checked_list)}")
    else:
        already_checked_list.append(user_letter)
        if user_letter in word:
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = value
            print(" ".join(word_list))
        else:
            count_lives += 1

if final_msg is None:
    print("You lost :(")
else:
    print(final_msg)
