from live import load_game, welcome
from GuessGame import play1
from MemoryGame import play2
from CurrencyRoulette import play3
from time import sleep
from art import *


def nickname():
    name = ""
    while len(name) < 3:
        name = str(input("Enter your nickname: "))
        if len(name) < 3:
            print("3 characters minimum! \
            Numbers and symbols can also be used")
    return name.replace(" ", "")


def menu():
    back = input("Back to menu? (y/n): ").lower()
    while back not in ["y", "n"]:
        print("Choose y or n only!")
        back = input("Back to menu? (y/n): ").lower()
    return back


tprint("-Welcome  To  WoG-")
name = nickname()
print(welcome(name))
back = "y"
while back == "y":
    option, difficulty = load_game()
    print(f"We start playing game number {option} on difficulty level {difficulty}")
    sleep(1)
    if option == "1":
        tprint("- Memory  Game -")
        play2(name, difficulty)
    elif option == "2":
        tprint("- Guess  Game -")
        play1(name, difficulty)
    elif option == "3":
        tprint("- Currency  Roulette -")
        play3(name, difficulty)
    back = menu()
    print()
else:
    print("See You Next Time!")
    sleep(3)
