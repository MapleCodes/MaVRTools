# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file contains the all the functions that are used for GUI. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import dotenv, os
import customtkinter as ctk

def dotENVHelper(dialog, subject):
    answer = dialog.get_input()
    dotenv.set_key(dotenv.find_dotenv(), subject, answer)

def dotENVDelete():
    os.remove(".env")
    open(".env", "w").close()

def dotENVDiscordBot():
    dialog = ctk.CTkInputDialog(title="Discord Token", text="Enter the relevant details")
    dotENVHelper(dialog, "DISCORD_TOKEN")

def dotENVOpenAI():
    dialog = ctk.CTkInputDialog(title="OpenAI Token", text="Enter the relevant details")
    dotENVHelper(dialog, "OPENAI_TOKEN")
