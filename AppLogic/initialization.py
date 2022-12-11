"""
This file contains all the first time setup.
Such as, creating the .env file, and setting up the tokens.

And more to be added in the future.
"""

import dotenv, os
import customtkinter as ctk

class fts:
    def __init__(self):
        if not os.path.exists(".env"):
            open(".env", "w").close()
            dotenv.set_key(dotenv.find_dotenv(), "DISCORD_TOKEN", '')
            dotenv.set_key(dotenv.find_dotenv(), "OPENAI_TOKEN", '')
            dialog = ctk.CTkInputDialog(title="First Time Setup", text="Please Enter your Discord ID!\n(Right click on yourself, and copy ID)")
            answer = dialog.get_input()
            dotenv.set_key(dotenv.find_dotenv(), "USER_TOKEN", answer)
        else:
            pass