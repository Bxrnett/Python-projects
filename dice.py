import random

def roll_dice(sides=6):
    result = random.randint(1, sides)
    return result

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    
    while True:
        input("Press Enter to roll the dice (or type 'exit' to quit): ")
        
        result = roll_dice(sides)
        print(f"You rolled a {result}")

        exit_command = input("Type 'exit' to quit, or press Enter to roll again: ")
        if exit_command.lower() == 'exit':
            break

if __name__ == "__main__":
    main()