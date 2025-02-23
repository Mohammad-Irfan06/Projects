Rock = '''
         ________
    ---'    ____ )
           (_____ )
           (_____ )
           (____ )
    ---.__(___ )
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game_images = [Rock,Paper,Scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors "))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("computer choose:")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif user_choice < computer_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")