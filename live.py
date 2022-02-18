def welcome(name):
    return f"Hello \033[1m{name}\033[0m and welcome to the World of Games.\n" \
           f"Here you can find many cool games to play.\n"


def load_game():
    option = input(
        f"Please choose a game to play:\n"
        f"1. Memory Game -  sequence of numbers will appear for 0.7 second and you have to guess it back\n"
        f"2. Guess Game - guess a number and see if you chose like the computer\n"
        f"3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    while option not in ['1', '2', '3']:
        print("Only numbers 1-3 can be selected")
        option = input(
            f"Please choose a game to play:\n"
            f"1. Memory Game -  sequence of numbers will appear for 0.7 second and you have to guess it back\n"
            f"2. Guess Game - guess a number and see if you chose like the computer\n"
            f"3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    level = input("Please choose game difficulty from 1 to 5: \n")
    while level not in ['1', '2', '3', '4', '5']:
        print("Only numbers 1-5 can be selected")
        level = input("Please choose game difficulty from 1 to 5: \n")

    return option, int(level)

