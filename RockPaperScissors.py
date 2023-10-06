from random import randint

def gen_computer_choice() -> str:
    """
    Generates a choice of rock/paper/scissors for the computer
    """
    choice = ""
    num = randint(1,3)
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    else:
        return "Scissors"
def get_user_choice() -> str:
    """
    Prompts the user for choice of rock/paper/scissors
    """
    user = input("Rock (R), Paper (P), or Scissors(S). Pick an option: ")
    if user.upper() == "R":
        return "Rock"
    elif user.upper() == "P":
        return "Paper"
    elif user.upper() == "S":
        return "Scissors"
        
    while user.upper() != "R" and user.upper() != "S" and user.upper() != "P":
        user = input("Invalid input! Please pick Rock (R), Paper (P), or Scissors(S).")
        if user.upper() == "R":
            return "Rock"
        elif user.upper() == "P":
            return "Paper"
        elif user.upper() == "S":
            return "Scissors"


def play_game(user: str, computer: str) -> None:
    """
    Shows the winner based on computer and users choice
    """
    
    if user == "Rock" and computer == "Rock":
        print(f"Tie game! You chose {user} & computer chose {computer}.")
    elif user == "Rock" and computer == "Paper":
        print(f"You lost! You chose {user} & computer chose {computer}.")
    elif user == "Rock" and computer == "Scissors":
        print(f"You won! You chose {user} & computer chose {computer}.")
    elif user == "Paper" and computer == "Paper":
        print(f"Tie game! You chose {user} & computer chose {computer}.")
    elif user == "Paper" and computer == "Rock":
        print(f"You won! You chose {user} & computer chose {computer}.")
    elif user == "Paper" and computer == "Scissors":
        print(f"You lost! You chose {user} & computer chose {computer}.")
    elif user == "Scissors" and computer == "Scissors":
        print(f"Tie game! You chose {user} & computer chose {computer}.")
    elif user == "Scissors" and computer == "Rock":
        print(f"You lost! You chose {user} & computer chose {computer}.")
    elif user == "Scissors" and computer == "Paper":
        print(f"You won! You chose {user} & computer chose {computer}.")
    
    option = input("Do you want to play again?(Y/N) ")   
    
    if option.upper() == "Y":
        main()
    elif option.upper() == "N":
        print("Play again soon!")
        
    while option.upper() != "Y" and option.upper() != "N":
        option = input("Invalid option! Do you want to play again?(Y/N) ")
        if option.upper() == "Y":
            main()
        elif option.upper() == "N":
            print("Play again soon!")
    
        
        
def main() -> None:
    """
    Calls the rest of the functions
    """
    computer_choice = gen_computer_choice()
    user_choice = get_user_choice()
    play_game(user_choice, computer_choice)
    
main()