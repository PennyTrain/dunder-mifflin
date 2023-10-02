# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from questions import office_questions
import gspread
from google.oauth2.service_account import Credentials
import random
import os
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('theOfficeQuestions')


def clear():
    """
    This clears the terminal ready for new content!
    """
    os.system("cls" if os.name == "nt" else "clear")

def initial_start():
    """
    This prints what the user first sees when they open the Dunder Mifflin quiz!
    It asks them if they are ready to play and if they are not it returnts to initial start.
    """
    clear()
    print("Are you ready the best Dunder Mifflin quiz?🥰\n")
    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡\n")
    print("Please press 's' when you are ready to start!")
    try:
        while True:
            return_to_menu = input("")
            if return_to_menu not in ["s"]:
                raise Exception
            else:
                main_menu()
    except Exception:
        print("""
                ༻✦༺ So sorry! ༻✦༺
         It appears you have not chosen 's' 
         and have entirely missed the mark 
        with something random! Please try again!
                      (✿◠‿◠)
         """)
        initial_start()

def main_menu():
    """
    This displays the main menu and runs the function menu_selection
    """
    clear()
    print(
        """
        ‿︵‿︵ʚ˚̣̣̣͙ɞ・❉  Main Menu  ❉・ ʚ˚̣̣̣͙ɞ‿︵‿︵\n
                         Play😍\n
                         Rules📃\n
                         Quit😰\n
        *+:｡.｡  Please type "p" to play  ｡.｡:+*
        *+:｡.｡  Please type "r" for rules  ｡.｡:+*
        *+:｡.｡  Please type "q" to quit  ｡.｡:+*
    """)
    menu_selection()

def rules():
    clear()
    print(
        """
              Rules
    ｡☆✼★━━━━━━━━━━━━★✼☆｡
    Once you have chosen your
    answer to a question please
    select 'a', 'b' or 'c'.
    Press 'm' to return to the 
           main menu!
    """)
    try:
        while True:
            return_to_menu = input("")
            if return_to_menu not in ["m"]:
                raise Exception
            else:
                main_menu()
    except Exception:
        print("""༻✦༺ So sorry! ༻✦༺
         It appears you have not chosen 'm' 
         and have entirely missed the mark 
        with something random! Please try again!
                      (✿◠‿◠)
         """)
        clear()
        main_menu()

def quit():
    clear()
    initial_start()

def quiz_management():
    clear()
    print("in quiz")
    question_amount = get_question_amount()
    username = get_username()
    score = 0
    get_question_randomer()

    
def get_question_randomer():
    random_question = random.choice(office_questions)
    print(random_question)

def get_username():
    """
    Gets the players username and ensures it is longer than 2 characters.
    """
    username = input("Enter username:")
    while True:
        if len(username) >= 2:
            print(f'Hello and welcome {username}!♥‿♥')
            break
        else:
            print("Any old username will do (⌒▽⌒)")
            break

def get_question_amount():
    """
    This function enables the player to choo
    """
    while True: 
        try:
            question_number = int(input("Please choose how many questions you would like! 5, 10 or 15?"))
            if question_number in [5, 10, 15]:
                print(f"You have chosen to have {question_number} questions!")
                break
            else:
                print("I'm sorry, that answer was not recognized! Please try putting 5, 10 or 15!")
        except ValueError:
            print("So sorry!!! Please try to enter a number!")

def menu_selection():
    """
    This function allows players to choose which option they would like!
    It also raises an exception if their input is not valid and recognized by the code.
    """
    try:
        while True:
            option = input("")
            if option not in ["p", "r", "q"]:
                raise Exception
            else:
                if option == 'p':
                    quiz_management()
                    break
                elif option == 'r':
                    rules()
                    break
                elif option == 'q':
                    initial_start()
                    break
    except Exception:
        clear()
        print('''༻✦༺ So sorry! ༻✦༺
        It appears you have not chosen 'p', 'r' 
        or 'q' and have entirely missed the mark 
        with something random! Please try again!
                      (✿◠‿◠)
         ''')
        user_main_menu()




initial_start()