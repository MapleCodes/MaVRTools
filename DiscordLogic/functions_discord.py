# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file contains the all the functions that are used for DCS. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import asyncio, discord, dotenv, os, time

# import TIER.trifork as TRIFORK # You won't have this one.
# import functions_env as FE
# import functions_vr as FVR
# import functions_controller as FC
# import functions_discord as FD
# import initialization as MINIT
# import UI.model as MODEL

from os import system
from pythonosc import *
from pythonosc.udp_client import SimpleUDPClient
from threading import Thread

def channel_type(self, message):
    # Checks if the message is sent in the server.
    if message.guild is not None:
        return message.channel.name

    # Checks if the message is sent in a DM.
    if message.guild is None:
        return "DM"

def message_filter(self, message):
    # Checks if the message is sent by a bot.
    if message.author.bot:
        return

    # Don't read our own messages.
    if message.author == self.user:
        return

    return True    

class Discord(discord.Client):
    def Invoked():
        DISCORDTOKEN = dotenv.get_key(dotenv.find_dotenv(), "DISCORD_TOKEN")
        CLIENT = Discord(intents=discord.Intents.all())
        CLIENT.run(DISCORDTOKEN)

    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with Maple#3668"))
        await self.get_user(dotenv.get_key(dotenv.find_dotenv(), "USER_TOKEN")).send(f"Logged on as {self.user}!") # This is me | Maple#3668

        print(f"Logged on as {self.user}!")

        global only_channels
        only_channels = ["DM"] # Add the channel here, will be modular in the future.


    async def on_message(self, message):
        current_channel = channel_type(self, message)
        
        if message_filter(self, message) is None or current_channel not in only_channels:
            return

        await message.channel.send(f"Hello {message.author.mention}!")