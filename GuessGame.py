from random import randint
from time import sleep
from art import *
from Score import *



def check_result():
    print("Let's see if you were right", end="")
    for i in range(3):
        sleep(1)
        print(".", end="")
    print()


def compare_results(lucky_number, secret_number, difficulty, name):
    if lucky_number == secret_number:
        print("\033[1m***YOU WIN***\033[0m")
        add_score(name, points_of_winning(difficulty))
        sleep(1)
    else:
        print("\033[1mYOU LOSE!\033[0m")
        sleep(1)


def if_one(difficulty):
    if difficulty != 1:
        return difficulty
    else:
        return difficulty + 1


def generate_number(difficulty):
    num = randint(1, difficulty)
    return num


def get_guess_from_user(difficulty):
    lucky_num = 0
    status = 0
    while lucky_num < 1 or lucky_num > difficulty:
        if status != 0: print(f"Only numbers 1-{difficulty} can be selected")
        try:
            lucky_num = int(input(f"Choose your lucky number between 1 to {difficulty}: "))
        except ValueError:
            pass
        status = 1
    return lucky_num


def play_again():
    again = input("Another game? (y/n): ").lower()
    while again not in ["y", "n"]:
        print("Choose y or n only!")
        again = input("Another game? (y/n): ").lower()
    return again


def play1(name, difficulty):
    again = "y"
    while again == "y":
        difficulty = if_one(difficulty)
        lucky_number = get_guess_from_user(difficulty)
        secret_number = generate_number(difficulty)
        check_result()
        compare_results(lucky_number, secret_number, difficulty, name)
        print(f"Your number is: {lucky_number}\nThe winning number is: {secret_number}\n")
        again = play_again()
    else:
        print("GOODBYE\n")
        sleep(1)
