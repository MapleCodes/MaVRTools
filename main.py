"""
Time Wasted: 4hrs
"""

import dotenv, os

# import tkinter
import customtkinter as ctk

import functions_basic as FB
import initialization as MINIT

### GLOBAL VARIABLES ###
FONT = "Segoe SD"
SIDE_BUTTON_FDATA = f"{FONT}", 12, "bold"

### GLOBAL VARIABLES ###


### MAIN WINDOW ###
app = ctk.CTk()  
app.geometry("1280x720")
app.title("Malunette")
# app.iconbitmap("TEST.ico")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue") 
### MAIN WINDOW ###


### LEFT PANEL ###
app.grid_rowconfigure(0, weight=1)

LEFT_PANEL = ctk.CTkFrame(app, width=300, corner_radius=0)
LEFT_PANEL.grid(column=0, row=0, rowspan=4 , sticky="nsew")
LEFT_PANEL.grid_rowconfigure(4, weight=1)

LP_LABEL_FRONTER = ctk.CTkLabel(LEFT_PANEL, text="$ Malunette", font=(f"{FONT}", 35, "bold"))
LP_LABEL_FRONTER.grid(column=0, row=0, padx=20, pady=(35, 35))

LP_BUTTON_DISCORD = ctk.CTkButton(LEFT_PANEL, text="DISCORD TOKEN", font=SIDE_BUTTON_FDATA, command=FB.dotENVDiscordBot)
LP_BUTTON_DISCORD.grid(column=0, row=1, padx=20, pady=(0, 20), ipadx=25, ipady=7)

LP_BUTTON_OPENAI = ctk.CTkButton(LEFT_PANEL, text="OPENAI TOKEN", font=SIDE_BUTTON_FDATA, command=FB.dotENVOpenAI)
LP_BUTTON_OPENAI.grid(column=0, row=2, padx=20, pady=(0, 20), ipadx=25, ipady=7)

LP_BUTTON_WEBCAPTIONER = ctk.CTkButton(LEFT_PANEL, font=SIDE_BUTTON_FDATA, text="WEBCAPTIONER")
LP_BUTTON_WEBCAPTIONER.grid(column=0, row=3, padx=20, pady=(0, 20), ipadx=25, ipady=7)

LP_BUTTON_DELETEENV = ctk.CTkButton(LEFT_PANEL, text="DELETE ALL KEYS", font=SIDE_BUTTON_FDATA, command=FB.dotENVDelete, fg_color="#ab1b25", hover_color="#8c1119")
LP_BUTTON_DELETEENV.grid(column=0, row=5, padx=20, pady=(0, 20), ipadx=25, ipady=7)

### LEFT PANEL ###


### MAIN APP ###
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=0)
app.grid_rowconfigure(1, weight=1)

MA_LABEL_TOP = ctk.CTkLabel(app, text="GENERAL OUTPUT / INPUT DISPLAY", font=(f"{FONT}", 20, "bold"))
MA_LABEL_TOP.grid(column=1, row=0, padx=20, pady=(20, 0), sticky="w")

MAIN_TABVIEW = ctk.CTkTabview(app)
MAIN_TABVIEW.grid(column=1, row=1, padx=20, pady=(0, 20), sticky="nsew")
MAIN_TABVIEW.add("Discord")
MAIN_TABVIEW.add("WebCaptioner")
MAIN_TABVIEW.add("ENV")

### MAIN APP ###


### START CONFIG ###
LP_BUTTON_WEBCAPTIONER.configure(state="disabled")
### START CONFIG ###


### BEGIN ###
MINIT.fts()
app.mainloop()
### BEGIN ###