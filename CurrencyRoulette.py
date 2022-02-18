import requests, json
from random import randint
from time import sleep
from Score import *



def get_money_interval():
    key = "32cfe8e0-62a6-11ec-b1f1-f16b3fd0271a"
    url = "https://freecurrencyapi.net/api/v2/latest?apikey=32cfe8e0-62a6-11ec-b1f1-f16b3fd0271a&base_currency=USD"
    resp = requests.get(url).text
    currency = json.loads(resp)["data"]["ILS"]
    number = randint(1, 100)
    return currency, number


def get_guess_from_user(number):
    valid = False
    while valid is not True:
        try:
            guess = int(input(f"How much is {number}$? "))
            if isinstance(guess, int):
                valid = True
            else:
                print("Only numbers can be selected")
        except ValueError:
            print("Only numbers can be selected")
    return guess


def check_answer(name, difficulty, guess, answer,):
    if (answer - (6 - difficulty)) <= guess <= (answer + (6 - difficulty)):
        print("***YOU WIN***")
        add_score(name, points_of_winning(difficulty))
    else:
        print("YOU LOSE!")


def check_result():
    print("Let's see if you were right", end="")
    for i in range(3):
        sleep(1)
        print(".", end="")
    print()


def play_again():
    again = input("Another game? (y/n): ").lower()
    while again not in ["y", "n"]:
        print("Choose y or n only!")
        again = input("Another game? (y/n): ").lower()
    return again


def play3(name, difficulty):
    again = "y"
    while again == "y":
        currency, number = get_money_interval()
        answer = int(currency * number)
        guess = get_guess_from_user(number)
        check_result()
        check_answer(name, difficulty, guess, answer)
        print(f"The answer: {answer}")
        print(f"Your guess: {guess}")
        print(f"The Currency is: {currency}\n")
        again = play_again()
        print()
    else:
        print("GOODBYE\n")
        sleep(1)
