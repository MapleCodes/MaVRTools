# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file contains the all the functions that are used for ENV. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import random
import dotenv, os
import customtkinter as ctk

def dotENVHelper(dialog, subject):
    answer = dialog.get_input()
    if answer == "":
        return
    dotenv.set_key(dotenv.find_dotenv(), subject, answer)

def dotENVDelete():
    randomNumber = random.randint(1, 100)
    dialog = ctk.CTkInputDialog(title="Delete .env", text=f"Are you sure you want to delete the .env file? \nType {randomNumber} to confirm.")
    try:
        answer = int(dialog.get_input())
    except ValueError:
        return

    if answer == randomNumber:
        os.remove(".env")
        open(".env", "w").close()
    elif answer == "N":
        return

def dotENVDiscordBot():
    dialog = ctk.CTkInputDialog(title="Discord Token", text="Enter the relevant details")
    dotENVHelper(dialog, "DISCORD_TOKEN")

def dotENVOpenAI():
    dialog = ctk.CTkInputDialog(title="OpenAI Token", text="Enter the relevant details")
    dotENVHelper(dialog, "OPENAI_TOKEN")

def dotENVTriFork():
    dialog = ctk.CTkInputDialog(title="First Set", text="Enter the relevant details")
    dotENVHelper(dialog, "TRIFORK_1")
    dialog = ctk.CTkInputDialog(title="Second Set", text="Enter the relevant details")
    dotENVHelper(dialog, "TRIFORK_2")
