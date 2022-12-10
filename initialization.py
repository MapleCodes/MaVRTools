"""
This file contains all the first time setup.
Such as, creating the .env file, and setting up the tokens.

And more to be added in the future.
"""

import dotenv, os

class fts:
    def __init__(self):
        if not os.path.exists(".env"):
            open(".env", "w").close()
        else:
            pass