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
    os.system("cls" if os.name == "nt" else "clear")

def initial_start():
    clear()
    print("Are you ready the best Dunder Mifflin quiz?🥰\n")
    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
    main_menu()

def main_menu():
    clear()
    print(
        """
        ‿︵‿︵ʚ˚̣̣̣͙ɞ・❉  Main Menu  ❉・ ʚ˚̣̣̣͙ɞ‿︵‿︵\n
                         Play😍\n
                         Rules📃\n
                         Quit😰\n
        *+:｡.｡  Please type "P" to play  ｡.｡:+*
        *+:｡.｡  Please type "R" for rules  ｡.｡:+*
        *+:｡.｡  Please type "Q" to quit  ｡.｡:+*
    """)

def rules():
    


def menu_selection():
    try:
        while True:


