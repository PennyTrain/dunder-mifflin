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
    os.system('cls' if os.name == 'nt' else 'clear')


def initial_start():
    """
    This prints what the user first sees when they
    open the Dunder Mifflin quiz!
    It asks them if they are ready to play
    and if they are not it returnts to initial start.
    """
    clear()
    print("Are you ready the best Dunder Mifflin quiz?🥰\n")
    print("Trivia all about The Office! The American")
    print("version!\n")
    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡\n")
    print("Please press 's' when you are ready to start!\n")
    while True:
        return_to_menu = input("").strip().lower()
        if return_to_menu == "s":
            main_menu()
            break
        else:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen 's'
Please try again!(✿◠‿◠)\n
                """)


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
                      LeaderBoard🏅\n
                         Quit😰\n
        *+:｡.｡  Please type "p" to play  ｡.｡:+*
        *+:｡.｡  Please type "r" for rules  ｡.｡:+*
        *+:｡.｡  Please type "l" for leaderboard  ｡.｡:+*
        *+:｡.｡  Please type "q" to quit  ｡.｡:+*\n
    """)
    menu_selection()


def rules():
    clear()
    print(
        """
              Rules
    ｡☆✼★━━━━━━━━━━━━━━★✼☆｡
    Once you have chosen your
    answer to a question please
    select 'a', 'b' or 'c'.
    Press 'm' to return to the
           main menu!\n
    """)
    while True:
        return_to_menu = input("").strip().lower()
        if return_to_menu == "m":
            main_menu()
            break
        else:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen 'm'
Please try again!(✿◠‿◠)\n
                """)


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
    game_ending = end_of_game(score, question_amount, username)


def get_username():
    """
    Gets the player's username and ensures it is longer than 2 characters.
    """
    while True:
        username = input("Enter username: ").strip().lower()
        if len(username) >= 2:
            print(f'Hello and welcome, {username}! ♥‿♥\n')
            return username
        else:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears your username is too
short Please try again!
        (✿◠‿◠)\n
                """)
        time.sleep(3.0)


def get_question_amount():
    """
    This function enables the player to choose
    the amount of questions they have!
    """
    valid_choices = [5, 10, 15]
    while True:
        try:
            question_amount = int(input("""
Please choose how many questions you would like! 5, 10 or 15?\n
            """))
            if question_amount in valid_choices:
                print(f"""
You have chosen to have 𓆩*𓆪 {question_amount} 𓆩*𓆪 questions!\n
""")
                return question_amount
            else:
                print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen '5',
 '10' or '15'  Please try again!
        (✿◠‿◠)\n
                """)
                time.sleep(3.0)
        except ValueError:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen '5',
 '10' or '15'  Please try again!
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
        """
        that prints the three choices in the question
        """
        for j, choice in enumerate(questions[i]["answers"]):
            print(f"{choice}")
        player_answer = get_player_input()
        answer_result = get_check_answer(questions[i])
        if player_answer == answer_result:
            print("Wooohoo! You got it right!ᕦ( ˘ᴗ˘ )ᕤ\n")
            score += 1
        else:
            print("Oh no you got it wrong, unlucky!(๑•́_•̀๑)\n")
        time.sleep(1.8)
        clear()
        i += 1
    return score
    


def get_player_input():
    print("Please select (a, b, c):\n")
    while True:
        try:
            player_answer = input("").strip().lower()
            if player_answer in ['a', 'b', 'c']:
                return player_answer
            else:
                raise Exception
        except Exception:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen 'a',
 'b' or 'c'  Please try again!
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


def end_of_game(score, question_amount, username):
    leaderboard_update(username, score, question_amount)
    print(f"""
★ ° . *   ° . °☆  . * ● , ● , .    ★
.    ★  ° :. ★  * • ○ ° ★ ★  * • ○ ° ★

             End Of Game!
.  *  .       .
°  . ● . ★ ° . *   ° . °☆ ★  * • ○ ° ★

Your score was: {score}/{question_amount}

 . * ● , .    ★  ° :●.   * ● , .    ★
• ○ ° ★  .  *  .       .★  * • ○ ° ★
   °  . ● . ★ ° . *   ° .:.☆★  *

Would you like to return to the main menu?
    If so please press 'm'

°☆  . * ● , .    ★ ● , .    ★ ● , .    ★
° :.   * • ○ ° ★  .  *  .
 ★   .   °  .  .     ★ ★  * • ○ ° ★ ° ★

    """)
    while True:
        return_to_menu = input("").strip().lower()
        if return_to_menu == "m":
            main_menu()
            break
        else:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen 'm',
Please try again!(✿◠‿◠)\n
                """)


def leaderboard_update(username, score, question_amount):
    if question_amount == 5:
        score_sheet_five = SHEET.worksheet('leaderboard-5')
        score_sheet_five.append_row([username, score])
    elif question_amount == 10:
        score_sheet_ten = SHEET.worksheet('leaderboard-10')
        score_sheet_ten.append_row([username, score])
    elif question_amount == 15:
        score_sheet_fifteen = SHEET.worksheet('leaderboard-15')
        score_sheet_fifteen.append_row([username, score])


def leaderboard_choice():
    clear()
    print("""
Which leaderboard would you like to view?
꒱࿐♡ ˚.*ೃ꒱࿐♡ ˚.*ೃ꒱࿐♡ ˚.*ೃ꒱࿐♡ ˚.*ೃ

            Leaderboard 1
                 ❁
      For all 5 question rounds

            Leaderboard 2
                 ❁
      For all 10 question rounds

            Leaderboard 3
                 ❁
      For all 15 question rounds

    """)
    leaderboard_selection()


def leaderboard_selection():
    while True:
        option = input("").strip().lower()
        if option not in ["5", "10", "15"]:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen '5',
 '10' or '15'  Please try again!
        (✿◠‿◠)\n
                """)
        else:
            if option == '5':
                users_choice = 5
                leaderboard_screen(users_choice)
            elif option == '10':
                users_choice = 10
                leaderboard_screen(users_choice)
            elif option == '15':
                users_choice = 15
                leaderboard_screen(users_choice)
            else:
                print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen '5',
 '10' or '15'  Please try again!
        (✿◠‿◠)\n
                """)
                continue


def get_scoresheet_list(rounds, position):
    """
    Gets the values of all the worksheets
    5 - 10 - 15 and puts them in ascending order
    """
    if rounds == 5:
        worksheet = SHEET.worksheet('leaderboard-5')
    elif rounds == 10:
        worksheet = SHEET.worksheet('leaderboard-10')
    elif rounds == 15:
        worksheet = SHEET.worksheet('leaderboard-15')
    worksheet_values = worksheet.get_all_values()
    score = worksheet_values
    length_score = len(score)
    for i in range(0, length_score):
        for j in range(0, length_score-i-1):
            if (int(score[j][1]) > int(score[j + 1][1])):
                tempo = score[j]
                score[j] = score[j + 1]
                score[j + 1] = tempo
    return score[length_score - (position)]


def leaderboard_screen(users_choice):
    clear()
    print("""
    ──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
»»———————-—★————————-««
      Leaderboard
»»———————-—★————————-««
    """)
    # THIS IS GETTING MY ARRAY OF FIRST SECOND AND THIRD PLACE AND PRINTING OUT
    first_place = get_scoresheet_list(users_choice, 1)
    second_place = get_scoresheet_list(users_choice, 2)
    third_place = get_scoresheet_list(users_choice, 3)
    print('First place is...')
    time.sleep(2.0)
    print(f'♕🥇  {first_place[0]}  ♕\n')
    time.sleep(1.0)
    print('Their score was...')
    time.sleep(2.0)
    print(f'{first_place[1]}\n')
    time.sleep(1.0)
    print('Second place is...')
    time.sleep(1.5)
    print(f'🥈  {second_place[0]}\n')
    time.sleep(1.0)
    print('Their score was...')
    time.sleep(1.5)
    print(f'{second_place[1]}\n')
    time.sleep(1.0)
    print('Third place is...')
    time.sleep(1.0)
    print(f'🥉  {third_place[0]}\n')
    time.sleep(1.0)
    print('Their score was...')
    time.sleep(1.0)
    print(f'{third_place[1]}\n')
    time.sleep(1.0)
    print("""
    When your done seeing the scores,
    press 'm' to return to the main
    menu!
    """)
    while True:
        return_to_menu = input("").strip().lower()
        if return_to_menu == "m":
            main_menu()
            break
        else:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen 'm',
Please try again!(✿◠‿◠)\n
                """)


def menu_selection():
    """
    This function allows players to choose
    which option they would like!
    It also raises an exception if their input
    is not valid and recognized by the code.
    """
    while True:
        option = input("").strip().lower()
        if option not in ["p", "r", "q", "l"]:
            print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen 'p',
 'r', 'l' or 'q'  Please try again!
        (✿◠‿◠)\n
                """)
        else:
            if option == 'p':
                quiz_management()
            elif option == 'r':
                rules()
            elif option == 'l':
                leaderboard_choice()
            elif option == 'q':
                initial_start()
            else:
                print("""
    ༻✦༺ So sorry! ༻✦༺
It appears you have not chosen 'p',
 'r', 'l' or 'q'  Please try again!
        (✿◠‿◠)\n
                """)
                continue


initial_start()
