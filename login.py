import time
import os
from games import *

startbalance = 100
userbalance = {}
users = {}
options1 = {"a": "Atm", "r": "Roulette", "f": "Flip", "c": "Crash", "q": "Log out"}
options2 = {"r": "Try again", "q": "Quit"}
optionsstart = {"login": "Login", "create": "Create user"}
optionsatm = {"withdraw": "Withdraw", "deposit": "Deposit", "check": "Check balance", "r": "Return"}
currentuser = ["element 0"]
tempinfo = []
# startar allting

def start():
    update("userinfo.txt", users)
    update("userbalance.txt", userbalance)
    if menu("Startmenu", "Choose", optionsstart) == "login":
        login(users, False)
    else:
        createUser()


# uppdaterar dicten med filen, kollar också att filen har en längd med fler än två element så det
# kan läggas i en dict


def update(file, dict):
    with open(file) as f:
        contents = f.readline().split()
        if len(contents) >= 2:
            for content in contents:
                index = contents.index(content)
                if not index % 2:
                    dict[content] = contents[index + 1]


# lägger till en lista i en fil


def addToFile(list, file, method):
    with open(file, method) as f:
        for item in list:
            f.write(f" {item} ")


# menyfunktionen, ger olika val beroende på vad man vill ha

def menu(title, prompt, options):
    action = ""
    print(title)
    print()
    for option in options:
        print(f"{option}) {options[option]}")
    while not action == "q":
        action = (str(input("Action: "))).lower()
        for n in options:
            if n == action:
                return n


# login sekvensen, kollar lösenord och användarnamn, kallar på meny om det är rätt

def login(users, firstlogin):
    if firstlogin:
        choice = menu("Casino", "Choice", options1)
        if choice == "a":
            atm(currentuser[0])
            return None
        if choice == "f":
            flip_(currentuser[0])
            return None
        if choice == "r":
            roulette_(currentuser[0])
            return None
    else:
        user = input("User: ")
        password = input("Password: ")
        for n in users:
            if n == user and users[n] == password:
                print("Welcome to Casino Cosmopol!")
                currentuser[0] = user
                time.sleep(1)
                choice = menu("Casino", "Choice", options1)
                if choice == "a":
                    atm(currentuser[0])
                    return n
                if choice == "f":
                    flip_(currentuser[0])
                    return n
                if choice == "r":
                    roulette_(currentuser[0])
                    return n
    while True:
        print()
        choice = menu("Invalid username or password", "Option: ", options2)
        if choice == "r":
            login(users, False)
            break
        elif choice == "q":
            return None

def bet_(user):
    while True:
        print(f"Current balance {userbalance[user]} $")
        bet = int(input("Choose bet amount: "))

        if type(bet) == int:
            if bet > int(userbalance[user]):
                print("Bet value too high, try again")
            else:
                return bet
        else:
            print("Not a number, try again")

def roulette_(user):
    bet = bet_(user)
    while True:
        color = input("What color, black, red or green: ")
        if color == "red":
            changebalance(user, -bet)
            win = roulette(bet, 10, 2)

            if win > 0:
                print("Congratulations!")
            else:
                print("Too bad.")
            changebalance(user, (bet * win))
            time.sleep(6)
            login(users, True)
        elif color == "black":
            changebalance(user, -bet)
            win = roulette(bet, 10, 1)

            if win > 0:
                print("Congratulations!")
            else:
                print("Too bad.")
            changebalance(user, (bet * win))
            time.sleep(6)
            login(users, True)
        elif color == "green":
            changebalance(user, -bet)
            win = roulette(bet, 10, 3)

            if win > 0:
                print("Congratulations!")
            else:
                print("Too bad.")
            changebalance(user, (bet * win))
            time.sleep(6)
            login(users, True)
        else:
            print("Try again")

def crash_(user):
    bet = bet_(user)
    guess = input("Guess the outcome, from 1-100: ")
    while True:
        if guess > 1 and guess < 100:
            changebalance(user, -bet)
            win = crash(bet, guess)
            if win > 0:
                print("Congratulations!")
            else:
                print("Too bad.")
            changebalance(user, (bet * win))
            time.sleep(6)
            login(users, True)
        else:
            print("Either not a value or not in range, try again")




def flip_(user):
    side = input("Choose side by typing red or black: ")
    bet = bet_(user)

    if side == "red":
        changebalance(user, -bet)
        win = flip(1)
        if win == 2:
            print("Congratulations!")
        else:
            print("Too bad.")
        changebalance(user, (bet * win))
        time.sleep(6)
        login(users, True)

    if side == "black":
        changebalance(user, -bet)
        changebalance(user, (bet * flip(0)))
        login(users, True)


# kollar om texten har ett ord i sig
def hasWord(word, text):
    if type(text) == "dict":
        for key in text:
            if key == word:
                return True
        return False


# skapar användare, lägger till i filen, lägger till pengar


def createUser():
    user = input("Name of user: ")
    password = input("Create password: ")
    password2 = input("Repeat password: ")
    if password == password2 and not hasWord(user, users):
        addToFile([user, password], "userinfo.txt", "a")
        addToFile([user, startbalance], "userbalance.txt", "a")
        update("userinfo.txt", users)
        update("userbalance.txt", users)
    start()


def changebalance(user, amount):
    f = open("userbalance.txt", "r")
    contents = f.readline().split()
    f.close()
    for word in contents:
        if word == user:
            contents[contents.index(word) + 1] = str(int(userbalance[word]) + int(amount))

    addToFile(contents, "userbalance.txt", "w")


def atm(currentuser):
        choice = menu("ATM", "Choice", optionsatm)
        if choice == "withdraw":
            f = open("userbalance.txt", "r")
            amountw = input("Amount to withdraw: ")
            contents = f.readline().split()
            f.close()
            for word in contents:
                if word == currentuser:
                    contents[contents.index(word)+1] = str(int(userbalance[word]) + int(amountw))

            addToFile(contents, "userbalance.txt", "w")
            atm(currentuser)
        elif choice == "deposit":
            f = open("userbalance.txt", "r")
            amountd = input("Amount to deposit: ")
            contents = f.readline().split()
            f.close()
            for word in contents:
                if word == currentuser:
                    contents[contents.index(word) + 1] = str(int(userbalance[word]) - int(amountd))

            addToFile(contents, "userbalance.txt", "w")
            atm(currentuser)
        elif choice == "check":
            print(f"{userbalance[currentuser]} $")
        elif choice == "r":
            login(users, True)


start()

