import random

from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo

print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
lives = 6

for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:
    print(f"****************************{lives} LIVES LEFT****************************")
    
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess in incorrect_letters:
        print(f'You\'ve already suggest letter: {guess}')

    if guess not in chosen_word and guess not in incorrect_letters:
        incorrect_letters.append(guess)
        lives -= 1
        print(stages[lives])

    print("The word is: ", display)

    if lives == 0:
        game_over = True
        print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
