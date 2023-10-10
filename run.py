# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from questions import office_questions
import gspread
from google.oauth2.service_account import Credentials
import time
import random
import os

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
    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡\n")
    print("Please press 's' when you are ready to start!\n")
    try:
        while True:
            return_to_menu = input("")
            if return_to_menu == "s":
                main_menu()
            else:
                raise Exception
    except Exception:
        print("""
                ༻✦༺ So sorry! ༻✦༺
         It appears you have not chosen 's' 
         and have entirely missed the mark 
        with something random! Please try again!
                      (✿◠‿◠)\n
         """)
        time.sleep(2.0)
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
        *+:｡.｡  Please type "q" to quit  ｡.｡:+*\n
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
           main menu!\n
    """)
    try:
        while True:
            return_to_menu = input("")
            if return_to_menu == "m":
                main_menu()
            else:
                raise Exception
    except Exception:
        print("""
                ༻✦༺ So sorry! ༻✦༺
         It appears you have not chosen 'm' 
         and have entirely missed the mark 
        with something random! Please try again!
                      (✿◠‿◠)\n
         """)
        time.sleep(3.0)
        main_menu()

def quit():
    """
    This enables the player to exit the quiz
    """
    clear()
    initial_start()

def quiz_management():
    """
    Here manages the quiz with what functions to run when the player enters.
    """
    clear()
    username = get_username()
    question_amount = get_question_amount()
    questions = get_question_randomer(question_amount)
    score = get_show_question(questions, question_amount)
    game_ending = end_of_game()

def get_username():
    """
    Gets the player's username and ensures it is longer than 2 characters.
    """
    while True:
        username = input("Enter username: ")
        if len(username) >= 2:
            print(f'Hello and welcome, {username}! ♥‿♥\n')
            return username
        else:
            print(
                """
                ༻✦༺ So sorry! ༻✦༺
         It appears you have not chosen a
         long enough username, and have entirely 
         missed the mark with something random! 
                 Please try again!
                      (✿◠‿◠)\n
         """)
        time.sleep(3.0)

def get_question_amount():
    """
    This function enables the player to choose the amount of questions they have!
    """
    valid_choices = [5, 10, 15]
    while True: 
        try:
            question_amount = int(input("Please choose how many questions you would like! 5, 10 or 15?\n"))
            if question_amount in valid_choices:
                print(f"You have chosen to have 𓆩*𓆪 {question_amount} 𓆩*𓆪 questions!\n")
                return question_amount
            else:
                print("""
                ༻✦༺ So sorry! ༻✦༺
         It appears you have not chosen between 5, 
         10 or 15 and have entirely missed the mark 
         with something random! Please try again!
                      (✿◠‿◠)\n
         """)
                time.sleep(3.0)
        except ValueError:
            print("""
                ༻✦༺ So sorry! ༻✦༺
         It appears you have not chosen between 5, 
         10 or 15 and have entirely missed the mark 
         with something random! Please try again!
                      (✿◠‿◠)\n
         """)
        time.sleep(3.0)
    
def get_question_randomer(question_amount):
    """
    This function gets a random question.
    """
    asked_questions = []
    questions = []
    while len(questions) < question_amount:
        x = random.randint(0, len(office_questions) - 1)
        if x not in asked_questions: 
            asked_questions.append(x)
            questions.append(office_questions[x])
    return questions

def get_show_question(questions, question_amount):
    i = 0
    score = 0
    while i < question_amount:
        print(questions[i]["question"]) 
        #that prints the three choices in the question
        for j, choice in enumerate(questions[i]["answers"]):
            print(f"{j + 1}. {choice}")
        player_answer = get_player_input()
        answer_result = get_check_answer(questions[i])
        if player_answer == answer_result:
            print("Wooohoo! You got it right!ᕦ( ˘ᴗ˘ )ᕤ\n")
            time.sleep(3.0)
            score += 1
        else:
            print("Oh no you got it wrong, unlucky!(๑•́_•̀๑)\n")
            time.sleep(3.0)
        i += 1
    return score

def get_player_input():
    print("Please select (a, b, c):\n")
    while True:
        try:
            player_answer = input("")
            if player_answer in ['a', 'b', 'c']:
                return player_answer
            else:
                raise Exception
        except Exception:
            print("""
                ༻✦༺ So sorry! ༻✦༺
         It appears you have not chosen between a, 
         b or c and have entirely missed the mark 
         with something random! Please try again!
                      (✿◠‿◠)\n
            """)
            time.sleep(3.0)
            
def get_check_answer(questions):
    if questions["correct"] == "a":
        return "a"
    elif questions["correct"] == "b":
        return "b"
    elif questions["correct"] == "c":
        return "c"

def end_of_game():
    clear()
    print(f"""
            End Of Game!
            Your score was: {score}/{question_amount}
    """)
    time.sleep(5.0)
    
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
        print('''
                ༻✦༺ So sorry! ༻✦༺
        It appears you have not chosen 'p', 'r' 
        or 'q' and have entirely missed the mark 
        with something random! Please try again!
                      (✿◠‿◠)\n
         ''')
        time.sleep(3.0)
        main_menu()

initial_start()

