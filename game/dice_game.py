import random
def dice_game():
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    
    print(f"You rolled: {user_roll}")
    print(f"Computer rolled: {computer_roll}")
    
    if user_roll > computer_roll:
        print("You win!")
    elif user_roll < computer_roll:
        print("Computer wins!")
    else:
        print("It's a tie!")