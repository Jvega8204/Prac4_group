print("welcome to Rock-Paper-Scissors!")  
player_choice = input("Enter Rock, Paper, or scissors: ").title()
print(f"You chose {player_choice}")

import random

options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)
print("Computer chooses:", computer_choice)
