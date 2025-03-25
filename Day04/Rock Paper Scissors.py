import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_board = [rock, paper, scissors]
user_choice  = int(input('Please choose 0 for Rock, 1 for Paper, 2 for Scissors: '))
computer_choice = random.randint(0,2)

if user_choice >= 0 and user_choice <= 2:
    print(f'Your choice is: \n{game_board[user_choice]}')
    print(f'Computer choice is: \n{game_board[computer_choice]}')

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
            print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")

else:
    print('Please type 0, 1 or 2')





