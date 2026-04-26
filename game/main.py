from stone_paper import stone_paper
from dice_game import dice_game
def main():
    while True:
        print("\n--- Game Menu ---")
        print("1. Stone-Paper-Scissors")
        print("2. Dice Roll Game")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            stone_paper()
        elif choice == "2":
            dice_game()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Try again.")


main()