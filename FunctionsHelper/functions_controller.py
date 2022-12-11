# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file contains the all the functions that are used for GUI. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import dotenv, os

# import TIER.trifork as TRIFORK # You won't have this one.
import FunctionsENV.functions_env as FE
import FunctionsHelper.functions_controller as FC
import FunctionsDiscord.functions_discord as FD
# import initialization as MINIT
# import main as MAIN

from threading import Thread

def StartApp():
    # use the config.ini file in the future, for now lets just complete the discord integration.
    if dotenv.get_key(dotenv.find_dotenv(), "DISCORD_TOKEN") == "":
        print("No Discord Token Found.")
        return

    # Run all of these in their own threads.
    # EG Discord = Thread(target=Discord, args=(discordToken,)).start()

    # Start the Discord bot.
    global DISCORD_RUNTIME
    DISCORD_RUNTIME = Thread(target=FD.Discord.Invoked, args=()).start()

def StopApp():
    # Stops all the threads.
    DISCORD_RUNTIME.stop()