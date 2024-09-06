"""
Simple program to create Rock_Paper_Scissors Game.
"""
import random


def comp_choice():
    result = ["Rock", "Paper", "Scissors"]  # Making list inclusive of choices to choose from, randomly.
    comp_result = random.choice(result)
    return comp_result


def game():
    global game_on  # Explicitly telling the program to use the global game_on

    while game_on:
        print("Press:\n"
              "1. for Rock\n"
              "2. for Paper\n"
              "3. for Scissors\n"
              "4. to Exit\n")

        user_choice = input("Enter your choice: ").strip()
        try:
            user_choice = int(user_choice)
            if 1 <= user_choice <= 4:
                if user_choice == 1 and comp_choice() == "Rock":
                    print(f"Computer chooses {comp_choice()}\n"
                          f"It's a draw. Let's Play Again!...\n\n")
                elif user_choice == 1 and comp_choice() == "Paper":
                    print(f"Computer chooses {comp_choice()}\n"
                          f"Computer Wins. Let's Play Again!...\n\n")
                elif user_choice == 1 and comp_choice() == "Scissors":  # User Win
                    print(f"Computer chooses {comp_choice()}\n"
                          f"Hurray {user_name} Wins. Let's Play Again!...\n\n")

                elif user_choice == 2 and comp_choice() == "Paper":
                    print(f"Computer chooses {comp_choice()}\n"
                          f"It's a draw. Let's Play Again!...\n\n")
                elif user_choice == 2 and comp_choice() == "Scissors":
                    print(f"Computer chooses {comp_choice()}\n"
                          f"Computer Wins. Let's Play Again!...\n\n")
                elif user_choice == 2 and comp_choice() == "Rock":  # User Win
                    print(f"Computer chooses {comp_choice()}\n"
                          f"Hurray {user_name} Wins. Let's Play Again!...\n\n")

                elif user_choice == 3 and comp_choice() == "Scissors":
                    print(f"Computer chooses {comp_choice()}\n"
                          f"It's a draw. Let's Play Again!...\n\n")
                elif user_choice == 3 and comp_choice() == "Rock":
                    print(f"Computer chooses {comp_choice()}\n"
                          f"Computer Wins. Let's Play Again!...\n\n")
                elif user_choice == 3 and comp_choice() == "Paper":  # User Win
                    print(f"Computer chooses {comp_choice()}\n"
                          f"Hurray {user_name} Wins. Let's Play Again!...\n\n")

                elif user_choice == 4:
                    game_on = False
                    print(f"Thanks for playing @ {user_name}.\n      See you soon!!...")
                    break

                else:
                    print("Invalid input.\nPlease try again.")
        except (ValueError, TypeError):
            print("Invalid input. Please enter a number (1-4).")


# Main program:

user_name = input("Enter your name: ").capitalize()

print(f"Welcome on Board!... @ {user_name} \n\n              Let's play Rock_Paper_Scissors")
global enter
try:

    enter = (input("Press 1 to enter the game or any other key to exit: "))
except ValueError:
    print("Invalid input. Please enter valid choice.")
    pass

if enter == "1":
    game_on = True
    game()
else:
    game_on = False
    print("Thank you for coming!!...")
