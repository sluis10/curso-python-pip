import random


def choose_options():
    options = ("piedra", "papel", "tijera")
    user_option = input("Piedra, Papel o Tijera: ").lower()
    computer_option = random.choice(options)

    if user_option not in options:
        print("Esa opción no es válida!\n")
        # continue
        return None, None

    print(f"User option => {user_option}")
    print(f"Computer option => {computer_option}")
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana contra Tijera")
            print("User ganó!")
            user_wins += 1
        else:
            print("Papel gana contra Piedra")
            print("Computer ganó!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana contra Piedra")
            print("User ganó!")
            user_wins += 1
        else:
            print("Tijera gana contra Papel")
            print("Computer ganó!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana contra Papel")
            print("User ganó!")
            user_wins += 1
        else:
            print("Piedra gana contra Tijera")
            print("Computer ganó!")
            computer_wins += 1
    return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
    if user_wins == 2:
        print("\nEl rotundo ganador es el usuario!")
        exit()

    if computer_wins == 2:
        print("\nEl rotundo ganador es la computadora!")
        exit()
  
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)

        print("computer_wins:", computer_wins)
        print("user_wins:", user_wins, "\n")

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        check_winner(user_wins, computer_wins)
        
        rounds += 1
        print("")

run_game()