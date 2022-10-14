import time
import os

startbalance = 100
userbalance = {}
users = {}
options1 = {"a": "Atm", "r": "Roulette", "b": "Blackjack", "c": "Crash", "q": "Log out"}
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
        login(users)
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

def login(users):
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
    while True:
        print()
        choice = menu("Invalid username or password", "Option: ", options2)
        if choice == "r":
            login(users)
            break
        elif choice == "q":
            return None


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
        elif choice == "deposit":
            f = open("userbalance.txt", "r")
            amountd = input("Amount to deposit: ")
            contents = f.readline().split()
            f.close()
            for word in contents:
                if word == currentuser:
                    contents[contents.index(word) + 1] = str(int(userbalance[word]) - int(amountd))

            addToFile(contents, "userbalance.txt", "w")
        elif choice == "check":
            print(f"{userbalance[currentuser]} $")
        elif choice == "r":
            menu("Casino", "Choice", options1)


start()

# addToFile(["hej", "test"], "userinfo.txt")
# with open("userinfo.txt", "r") as f:
# print(f.readline())
