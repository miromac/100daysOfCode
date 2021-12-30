import random

water_well = '''
    ______
---' _\ ___)
    \__|____)
      (_____)
---'__(____)
'''
paper = '''
    ______
---'   ___)___
       ________)
      (__________)
      (_________)
---'_________)
'''

scissors = '''
_ _ _ _________
    \ _\_______)_
     \__|________)
      |_/_)
---'___)
'''

game_images = [water_well, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Water well, 1 for Paper, 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)

print(f"Computer chose {computer_choice}\n")
print(game_images[computer_choice])

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