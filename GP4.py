#Travel agent part 2
#Author: Anna Fong and Kaitlyn Lum
#Date: July 28, 2023

#travel agent part 2

import random


#function that welcomes the user
def welcome():
    print('Welcome! I am your friendly travel agent bot.\n'\
    'I will ask you some questions, and make a\nrecommendation based on'\
    ' your answer.\nIf you are interested, I will provide you\n'\
    'with a one - time password to create a user\naccount on our website.\n')


def ask_number(question):
    answer = int(input(question))
    return answer

#ask user for their information
def ask_user_information ():
    # Ask user for name and greet user
    userName = input("What is your name? --> ")
    print("Hello dear " + userName + "!\n")

    ask_number("What is your age? --> ")
    # Ask user for age
    #defuserAge = int(input("What is your age? --> "))
    ask_number("\nFor how many nights do you want to stay? --> ")
    # Ask user how many nights they want to stay
    userNights = int(input("\nFor how many nights do you want to stay? --> "))

    return userName, userNights, userAge

global music

global beaches

def ask_user_preferences():

    # Ask whether the user is interested in culture and classical music, or beaches and surfing
    userCulture = input("Do you like culture and classical music?\nPlease answer y/n. --> ")
    userActivity = input("Do you like beaches and surfing?\nPlease answer y/n. --> ")

    # Make recommendations based on user's responses
    # If user prefers culture over beach, recommend trip to Vienna

    if userCulture == 'y':
        music = True
    else: 
        music = False
    if userActivity == 'y':
        beaches = True
    else:
        beaches = False
    return music, beaches

def ask_yesno():
    print("hi")




def compute_discountpercentage():
    print("hi")


def compute_totalcost():
    print("hi")


def show_tripdetails():
    print("hi")

def suggest_trip():
    print("hi")


def ask_2_create_account():
    print("hi")


#call functions
welcome()
ask_user_information()
print(ask_user_preferences())