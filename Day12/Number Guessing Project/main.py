from art import logo
import random

random_number = int(random.randint(1, 100))

print('Welcome to number Guessing Game!')
print('I am thinking of a number between 1 and 100')


def easy_game():
    attempts_count = 10
    print(f'You have {attempts_count} attempts')
    game_board(attempts = attempts_count)

def hard_game():
    attempts_count = 3
    print(f'You have {attempts_count} attempts')
    game_board(attempts=attempts_count)

def game_board(attempts):

    print(random_number)
    guess = 0
    while guess != random_number and attempts > 0:
        try:
            guess = int(input('Make a guess: '))
        except ValueError:
            print("You did not enter a number, please re-enter")
            continue
        if guess > random_number:
            attempts -= 1
            print('Too high')
            print(f'You have {attempts} attempts left')
        if guess < random_number:
            attempts -= 1
            print('Too low')
            print(f'You have {attempts} attempts left')


    if attempts == 0:
        print(f"\nGame Over.\nThe number was {random_number}")
    if guess == random_number:
        print(f"\nYou win.\nThe number was {random_number}")

print (logo)
difficulty = input('Choose difficulty. Type \'easy\' or \'hard\': ')

if difficulty == 'easy':
    easy_game()
if difficulty == 'hard':
    hard_game()
if difficulty != 'hard' or difficulty != 'easy':
    print('You did print mistake, try again')