import random

def get_random_choice():
    robot_choices = ["rock", "paper", "scissors"]
    return random.choice(robot_choices)

def main():
    print("Welcome to Rock Paper Scissors")

    print("Please enter your username: ")
    username = input()


    print("Thank you " + username)
    print("Please select Rock, Paper or Scissors:")
    answer = input()
    if answer not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return
    
    robot_selection = get_random_choice()

    print(f"You chose: {answer}")
    print(f"Computer chose: {robot_selection}")

    if answer == robot_selection:
        print("It's a tie!")
    elif (
        (answer == "rock" and robot_selection == "scissors") or
        (answer == "paper" and robot_selection == "rock") or
        (answer == "scissors" and robot_selection == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")
main()
