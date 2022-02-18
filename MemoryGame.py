from time import sleep
from random import randint
from tkinter import *
import tkinter as tk
from art import *
from Score import *


def generate_sequence(difficulty):
    get_ready()
    numbers = []
    for i in range(difficulty):
        numbers.append(randint(1, 101))
    root = Tk()
    root.attributes("-topmost", True)
    root.attributes("-fullscreen", True)
    canvas = Canvas(root)
    canvas.create_text(750, 350, fill="black", font="Times 40 italic bold",
                       text=", ".join([str(int) for int in numbers]))
    canvas.pack(fill=tk.BOTH, expand=True)
    root.after(700, root.destroy)
    root.mainloop()
    return numbers


def get_list_from_user(numbers):
    user_list = []
    for i in range(len(numbers)):
        valid = False
        while valid is not True:
            try:
                diff = int(input("Enter your guesses one by one: "))
                if 1 <= diff <= 101:
                    user_list.append(diff)
                    valid = True
                else:
                    raise ValueError("Only numbers 1-100 can be selected")
            except ValueError:
                print("Only numbers 1-101 can be selected")
    return user_list


def is_list_equal(numbers, user_list, name, difficulty):
    user_list.sort()
    numbers.sort()
    if user_list == numbers:
        print("***YOU WIN***")
        add_score(name, points_of_winning(difficulty))
        sleep(1)
    else:
        print("YOU LOSE!")
        sleep(1)


def get_ready():
    print("Get ready", end="")
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


def play2(name, difficulty):
    again = "y"
    while again == "y":
        numbers = generate_sequence(difficulty)
        user_list = get_list_from_user(numbers)
        is_list_equal(numbers, user_list, name, difficulty)
        print(f"Lucky numbers: {numbers}")
        print(f"Your numbers: {user_list}\n")
        again = play_again()
    else:
        print("GOODBYE\n")
        sleep(1)
