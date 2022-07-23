import random
import string
import time
def get_valid_word():
    words = []
    word = random.choice(words).upper()
    while '_' in word or '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word
def hangman():
    word = get_valid_word().upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        print("you have:", lives, " you have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_list))
        print("")
        user_letter = input("Guess a letter::").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
            print("ho ho you have already used the letter. Try again later")
        else:
            print("")
            print("Enter a valid letter.")
    if lives == 0:
        print("")
        print("you have lost the game. The word is :", word)
    else:
        print("")
        print("you have guessed the word:", word)
    print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")


print("\n**************************************************\n")
print("THIS SOFTWARE IS DEVELOPED BY DUMPA BHARGAV REDDY")
print("\n**************************************************")
while True:
    print("")
    a = input("Let's start the Game... Are you ready.. Y/N:").upper()
    if a == 'Y':
        hangman()
    elif a == 'N':
        print("Have a nice day .. Bye...")
        time.sleep(1.5)
        break
    else:
        print("")
        print("invalid option...Enter Y or N:")
print("\n**************************************************")
