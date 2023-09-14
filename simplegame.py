import random

# Define ASCII art images for rock, paper, and scissors
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

# Store the images in a list for easy access
game_images = [rock, paper, scissors]

# Get user input for their choice
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Check if the user input is valid
if user_input >= 3 or user_input < 0:
    print("You typed an invalid number, you lose!")
else:
    # Display the user's choice
    print("You chose:")
    print(game_images[user_input])

    # Generate a random choice for the computer
    computer_choice = random.randint(0, 2)
    
    # Display the computer's choice
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the game result based on choices
    if user_input == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_input == 2:
        print("You lose")
    elif computer_choice > user_input:
        print("You lose")
    elif user_input > computer_choice:
        print("You win!")
    elif computer_choice == user_input:
        print("It's a draw")
