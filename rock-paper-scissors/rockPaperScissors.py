
import random

game_choices=["Rock" , "Paper", "Scissors"]

def game():

    player_choice=input("\nRock, Paper or Scissors?\n").capitalize()
    print(f"\nYour choice is {player_choice}")

    if player_choice in game_choices:
        
        computer_choice=random.choice(game_choices)
        print(f"Computer choice is {computer_choice}\n")

        if player_choice == game_choices[0]:
            if computer_choice == game_choices[0]:
                print("It's a draw.")
            elif computer_choice == game_choices[1]:
                print("Paper covers Rock. Computer wins.")
            elif computer_choice == game_choices[2]:
                print("Rock smashes Scissors. You win.")

        elif player_choice == game_choices[1]:
            if computer_choice == game_choices[1]:
                print("It's a draw.")
            elif computer_choice == game_choices[2]:
                print("Scissors cuts Paper. Computer wins.")
            elif computer_choice == game_choices[0]:
                print("Paper covers Rock. You win.")
 
        elif player_choice == game_choices[2]:
            if computer_choice == game_choices[2]:
                print("It's a draw.")
            elif computer_choice == game_choices[0]:
                print("Rock smashes Scissors. Computer wins.")
            elif computer_choice == game_choices[1]:
                print("Scissors cuts Paper. You win.")

    else:
        print("Invalid choice, please try again.")

# Main Function
def main():
    while True:
        print("\nRock, Paper or Scissors\n")
        print("1. Let's play")
        print("2. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            game()
        elif choice == "2":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")

main()