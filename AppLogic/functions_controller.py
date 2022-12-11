# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file contains the all the functions that are used for GUI. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import dotenv, os, asyncio

# import TIER.trifork as TRIFORK # You won't have this one.
import dotENVLogic.functions_env as FE
import DiscordLogic.functions_discord as FD
# import initialization as MINIT
# import main as MAIN

from threading import Thread

class Start:
    def __init__(self):
        # use the config.ini file in the future, for now lets just complete the discord integration.
        if dotenv.get_key(dotenv.find_dotenv(), "DISCORD_TOKEN") == "":
            print("No Discord Token Found.")
            return

        # Run all of these in their own threads.
        # EG Discord = Thread(target=Discord, args=(discordToken,)).start()

        # Start the Discord bot.
        global DISCORD_RUNTIME, DISCORD_OBJECT
        DISCORD_OBJECT = FD.Discord
        DISCORD_RUNTIME = Thread(target=DISCORD_OBJECT.Invoked, args=()).start()

def StopApp():
    # Stops all the threads.
    DISCORD_RUNTIME.stop()