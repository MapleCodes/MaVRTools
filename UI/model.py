"""
Time Wasted: 12 hrs
"""

import dotENVLogic.functions_env as FE
import AppLogic.functions_controller as FC
import DiscordLogic.functions_discord as FD
import AppLogic.initialization as MINIT
import UI.function_display as FDisplay
# import main as MAIN

import dotenv, os, asyncio, sys
import customtkinter as ctk
import threading
from threading import Thread

from typing import TYPE_CHECKING

class model(ctk.CTk):
    def __init__(self, message=None, **FLOATERS):
        self.message=message # not used.

        if (threading.current_thread().name == "MainThread" and TYPE_CHECKING == False):
            self.CALL()

    def CALL(self):
        ### GLOBAL VARIABLES ###
        self.FONT = "Segoe SD"
        self.SIDE_BUTTON_FDATA = f"{self.FONT}", 12, "bold"

        ### END GLOBAL VARIABLES ###


        ### MAIN WINDOW ###
        self.app = ctk.CTk()  
        self.app.geometry("1280x720")
        self.app.title("Malunette")
        # app.iconbitmap("TEST.ico")

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue") 

        ### END MAIN WINDOW ###

        ### INLINE VARIABLES ###
        self.LP_SWITCH_VAR = ctk.StringVar(value="off")

        ### END INLINE VARIABLES ###

        ### LEFT PANEL ###
        self.app.grid_rowconfigure(0, weight=1)

        self.LEFT_PANEL = ctk.CTkFrame(self.app, width=300, corner_radius=0)
        self.LEFT_PANEL.grid(column=0, row=0, rowspan=10 , sticky="nsew")
        self.LEFT_PANEL.grid_rowconfigure(10, weight=1)

        self.LP_LABEL_FRONTER = ctk.CTkLabel(self.LEFT_PANEL, text="$ Malunette", font=(f"{self.FONT}", 35, "bold"))
        self.LP_LABEL_FRONTER.grid(column=0, row=0, padx=20, pady=(35, 35))

        self.LP_BUTTON_DISCORD = ctk.CTkButton(self.LEFT_PANEL, text="DISCORD TOKEN", font=self.SIDE_BUTTON_FDATA, command=FE.dotENVDiscordBot)
        self.LP_BUTTON_DISCORD.grid(column=0, row=1, padx=20, pady=(0, 20), ipadx=25, ipady=7)

        self.LP_BUTTON_OPENAI = ctk.CTkButton(self.LEFT_PANEL, text="OPENAI TOKEN", font=self.SIDE_BUTTON_FDATA, command=FE.dotENVOpenAI)
        self.LP_BUTTON_OPENAI.grid(column=0, row=2, padx=20, pady=(0, 20), ipadx=25, ipady=7)

        self.LP_BUTTON_WEBCAPTIONER = ctk.CTkButton(self.LEFT_PANEL, font=self.SIDE_BUTTON_FDATA, text="WEBCAPTIONER")
        self.LP_BUTTON_WEBCAPTIONER.grid(column=0, row=3, padx=20, pady=(0, 20), ipadx=25, ipady=7)

        self.LP_BUTTON_TRIFORK = ctk.CTkButton(self.LEFT_PANEL, text="TRIFORK KEY", font=self.SIDE_BUTTON_FDATA, command=FE.dotENVTriFork)
        self.LP_BUTTON_TRIFORK.grid(column=0, row=4, padx=20, pady=(0, 20), ipadx=25, ipady=7)

        # # # # #

        self.LP_SWITCH_DELETEENV = ctk.CTkSwitch(self.LEFT_PANEL, text="Enable Delete", font=self.SIDE_BUTTON_FDATA, command=self.LP_SWITCH_DELETEENV_FUNCTION, variable=self.LP_SWITCH_VAR, onvalue="on", offvalue="off")
        self.LP_SWITCH_DELETEENV.grid(column=0, row=11, padx=(0, 75), pady=(0, 20))

        self.LP_BUTTON_DELETEENV = ctk.CTkButton(self.LEFT_PANEL, text="DELETE .ENV CONFIG", font=self.SIDE_BUTTON_FDATA, command=FE.dotENVDelete, fg_color="#ab1b25", hover_color="#8c1119")
        self.LP_BUTTON_DELETEENV.grid(column=0, row=12, padx=20, pady=(0, 20), ipadx=25, ipady=7)

        self.LP_BUTTON_STOP = ctk.CTkButton(self.LEFT_PANEL, text="STOP", font=self.SIDE_BUTTON_FDATA, command=FC.StopApp, fg_color="#b3730c", hover_color="#6b4506")
        self.LP_BUTTON_STOP.grid(column=0, row=13, padx=20, pady=(0, 20), ipadx=25, ipady=7)

        self.LP_BUTTON_START = ctk.CTkButton(self.LEFT_PANEL, text="START ALL", font=self.SIDE_BUTTON_FDATA, command=FC.StartApp, fg_color="#1e9400", hover_color="#236912")
        self.LP_BUTTON_START.grid(column=0, row=14, padx=20, pady=(0, 20), ipadx=25, ipady=7)

        # # # # #

        ### END LEFT PANEL ###


        ### MAIN APP ###
        self.app.grid_columnconfigure(1, weight=1)
        self.app.grid_rowconfigure(0, weight=0)
        self.app.grid_rowconfigure(1, weight=1)

        self.MA_LABEL_TOP = ctk.CTkLabel(self.app, text="OUTPUT / INPUT DISPLAY", font=("Consolas", 20, "bold"))
        self.MA_LABEL_TOP.grid(column=1, row=0, padx=20, pady=(20, 0), sticky="w")

        self.MAIN_TABVIEW = ctk.CTkTabview(self.app)
        self.MAIN_TABVIEW.grid(column=1, row=1, padx=20, pady=(0, 20), sticky="nsew")
        self.MAIN_TABVIEW.add("Discord")
        # self.MAIN_TABVIEW.add("WebCaptioner")
        # self.MAIN_TABVIEW.add("TriFork")

        #region Discord TABVIEW
        self.DISCTAB_TEXTBOX_OUTPUT = ctk.CTkTextbox(self.MAIN_TABVIEW.tab('Discord'), font=("Consolas", 12))
        self.MAIN_TABVIEW.tab('Discord').grid_columnconfigure(0, weight=1)
        self.MAIN_TABVIEW.tab('Discord').grid_rowconfigure(0, weight=1)

        self.DISCTAB_TEXTBOX_OUTPUT.grid(column=0, row=0, padx=20, pady=(0, 20), sticky="nsew", columnspan=2)
        self.DISCTAB_TEXTBOX_OUTPUT.insert("end", "< Waiting for Connection >\n")
        self.DISCTAB_TEXTBOX_OUTPUT.configure(state="disabled")

        self.DISCTAB_TEXTBOX_INPUT = ctk.CTkTextbox(self.MAIN_TABVIEW.tab('Discord'), font=(f"{self.FONT}", 12), height=20)
        self.DISCTAB_TEXTBOX_INPUT.grid(column=0, row=1, padx=(20, 0), pady=(0, 20), sticky="nsew")
        self.DISCTAB_TEXTBOX_INPUT.bind("<Return>", self.DISCTAB_TEXTBOX_SEND_BIND)

        self.DISCTAB_BUTTON_SEND = ctk.CTkButton(self.MAIN_TABVIEW.tab('Discord'), text="SEND", font=self.SIDE_BUTTON_FDATA, command=self.DISCTAB_TEXTBOX_SEND, fg_color="#1e9400", hover_color="#236912")
        self.DISCTAB_BUTTON_SEND.grid(column=1, row=1, padx=20, pady=(0, 20), ipadx=25, ipady=5)

        #endregion


        ### END MAIN APP ###


        ### START CONFIG ###
        self.LP_BUTTON_WEBCAPTIONER.configure(state="disabled")
        self.LP_BUTTON_TRIFORK.configure(state="disabled")
        self.LP_BUTTON_DELETEENV.configure(state="disabled")

        ### END START CONFIG ###

        ### BEGIN ###
        if (threading.current_thread().name == "MainThread"):
            # Check for first time launching.
            MINIT.fts()

            logWidget = FDisplay.Display(self.DISCTAB_TEXTBOX_OUTPUT)
            sys.stdout = logWidget
            # sys.stderr = logWidget # not in use, maybe.
            
            self.app.mainloop()
        ### END BEGIN ###

    ### INLINE FUNCTIONS ###
    def LP_SWITCH_DELETEENV_FUNCTION(self):
        if self.LP_SWITCH_VAR.get() == "off":
            self.LP_BUTTON_DELETEENV.configure(state="disabled")
        elif self.LP_SWITCH_VAR.get() == "on":
            self.LP_BUTTON_DELETEENV.configure(state="normal")

    def DISCTAB_TEXTBOX_SEND(self):
        message = self.DISCTAB_TEXTBOX_INPUT.get("0.0", "end")[:-1]
        message = message.replace("\n", "")
        self.DISCTAB_TEXTBOX_INPUT.delete("0.0", "end")
        if message.__len__() > 0:
            self.DISCTAB_TEXTBOX_OUTPUT.configure(state="normal")
            self.DISCTAB_TEXTBOX_OUTPUT.insert("end", f"YOU: {message}\n")
            self.DISCTAB_TEXTBOX_INPUT.delete("0.0", "end")
            self.DISCTAB_TEXTBOX_OUTPUT.configure(state="disabled")

    # Something wrong with Tkinter and binds. This is a workaround.
    def DISCTAB_TEXTBOX_SEND_BIND(self, events):
        message = self.DISCTAB_TEXTBOX_INPUT.get("0.0", "end")[:-1]
        if message == "\n":
            self.DISCTAB_TEXTBOX_INPUT.delete("0.0", "end")
            return
        
        self.DISCTAB_TEXTBOX_SEND()
        self.DISCTAB_TEXTBOX_INPUT.delete("0.0", "end")
        # DISCTAB_BUTTON_SEND.destroy()

    ### END INLINE FUNCTIONS ###


    

