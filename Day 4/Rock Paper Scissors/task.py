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
game_images=[rock,paper,scissors]

user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
if user_input >=0 and user_input <=2:
    print(game_images[user_input])
# 0,1,2
computer_choice=random.randint(0,2)
print("computer choose:")
print(game_images[computer_choice])
if user_input>3 or user_input<0:
    print("Not Valid input. You loose.")
elif user_input==0 and computer_choice==2:
    print("You Win!")
elif computer_choice==0 and user_input==2:
    print("You Loose")
elif user_input > computer_choice:
    print("You Win!")
elif computer_choice > user_input:
    print("You Loose")
elif user_input == computer_choice:
    print("Draw")

